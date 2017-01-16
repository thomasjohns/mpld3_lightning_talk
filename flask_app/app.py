import random
import mpld3
import matplotlib.pyplot as plt
from flask import Flask

plt.style.use('ggplot')

app = Flask(__name__)


def generate_random_walk():
    xs = list(range(100))
    choices = [-1, 1]
    ys = [random.choice(choices)]
    for i in range(1, len(xs)):
        ys.append(ys[i - 1] + random.choice(choices))

    fig, ax = plt.subplots()
    ax.plot(xs, ys, '-y', linewidth=3)
    ax.set_ylim([-15, 15])
    return mpld3.fig_to_html(fig)


@app.route('/')
def home():
    return 'add /random_walk to the url'


@app.route('/random_walk')
def random_walk():
    html = generate_random_walk()
    return html


if __name__ == '__main__':
    app.run()
