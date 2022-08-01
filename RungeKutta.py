from matplotlib import pyplot as plt
from Function import implicit

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


def iterate(h, p: Point):
    a = implicit(p)
    b = implicit(Point(p.x + h / 2, p.y + a * h / 2))
    c = implicit(Point(p.x + h / 2, p.y + b * h / 2))
    d = implicit(Point(p.x + h, p.y + h * c))
    p.x, p.y = p.x + h, p.y + h / 6 * (a + 2 * b + 2* c + d)


def generate_axes(a, b, y, n):
    h = (b - a) / n
    p = Point(a, y)
    x_axis, y_axis = [p.x], [p.y]
    print('Before:', p)
    while p.x < b - h:
        iterate(h, p)
        x_axis.append(p.x)
        y_axis.append(p.y)
    print('After:', p)
    return x_axis, y_axis


def plot_result(dep, indep):
    plt.plot(dep, indep)
    plt.show()


def full(a, b, y, n):
    x_axis, y_axis = generate_axes(a, b, y, n)
    plot_result(x_axis, y_axis)


def main():
    with open('Function.py', 'w') as f:
        f.write('from Point import Point\nimport math\n\ndef implicit(p: Point):\n\treturn ')
        f.write(input('Input the Python expression you want to be differentiated. ').replace('x', 'p.x').replace('y', 'p.y'))
    full(float(input('Enter the starting x-coordinate of the realisation. ')), 
                float(input('Enter the ending x-coordinate of the realisation. ')), 
                float(input('Enter the starting y-coordinate of the realisation. ')), 
                float(input('Enter the number of samples you wish to take. ')))


if __name__ == '__main__':
    main()
