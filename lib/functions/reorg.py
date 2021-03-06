import chainer.functions as F


def reorg(input, stride=2):
    batch_size, input_channel, input_height, input_width = input.data.shape
    output_height, output_width, output_channel = int(input_height / stride), int(
        input_width / stride), input_channel * stride * stride
    output = F.transpose(F.reshape(input, (batch_size, input_channel, output_height, stride, output_width, stride)),
                         (0, 1, 2, 4, 3, 5))
    output = F.transpose(F.reshape(output, (batch_size, input_channel, output_height, output_width, -1)),
                         (0, 4, 1, 2, 3))
    output = F.reshape(output, (batch_size, output_channel, output_height, output_width))
    return output
