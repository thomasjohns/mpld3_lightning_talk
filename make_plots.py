import random
import matplotlib.pyplot as plt
import mpld3

plt.style.use('ggplot')


def generate_data():
    xs = []
    ys = []
    for i in range(1000):
        xs.append(i)
        ys.append(random.randint(0, 100))
    return xs, ys


def make_scatter_plot(xs, ys):
    fig, ax = plt.subplots()
    ax.plot(xs, ys, 'bo', alpha=.8)
    ax.set_ylim([0, 100])
    mpld3.save_html(fig, 'scatter.html')


def make_histogram(xs, ys):
    fig, ax = plt.subplots()
    ax.hist(ys)
    mpld3.save_html(fig, 'histogram.html')


def make_line_plot(xs, ys):
    fig, ax = plt.subplots()
    ax.plot(xs, ys, 'g-', alpha=.8)
    ax.set_ylim([0, 100])
    mpld3.save_html(fig, 'line_plot.html')


def main():
    xs, ys = generate_data()
    make_scatter_plot(xs, ys)
    make_histogram(xs, ys)
    make_line_plot(xs, ys)


if __name__ == '__main__':
    main()
