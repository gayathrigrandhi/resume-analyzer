import matplotlib.pyplot as plt

def skill_chart(matched, missing):

    labels = ['Matched Skills', 'Missing Skills']
    values = [len(matched), len(missing)]

    fig, ax = plt.subplots()

    ax.bar(labels, values)

    ax.set_title("Skill Match Analysis")
    ax.set_ylabel("Number of Skills")

    return fig