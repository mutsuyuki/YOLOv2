import cupy as xp
from chainer import Variable, gradient_check, testing
from sum_of_squared_error import *

batch_size = 32
n_input = 10

x_data = xp.random.randn(batch_size, n_input).astype(xp.float32)
t_data = xp.zeros(x_data.shape, dtype=xp.float32)
for i in range(batch_size):
    t_data[i][xp.random.randint(n_input)] = 1

x = Variable(x_data)
t = Variable(t_data)
y = sum_of_squared_error(x, t)

# backward to compute dy/dx
y.grad = xp.ones(y.data.shape, dtype=xp.float32)
y.backward()

# compute numerical grad
f = lambda: (sum_of_squared_error(x_data, t_data).data,)
gx, = gradient_check.numerical_grad(f, (x.data,), (y.grad,))

testing.assert_allclose(gx, x.grad)
