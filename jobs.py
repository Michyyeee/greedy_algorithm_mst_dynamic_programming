def read(filename):
    file = open(filename, 'r')
    data = file.readlines()

    jobs = []

    for line in data[1:]:
        items = line.split()
        jobs.append([int(items[0]), int(items[1])])

    return jobs


def order(jobs, key = 'difference' or 'ratio'):
    if key == 'difference':
        priority = [(item[0] - item[1], item[0]) for item in jobs]
    else:
        priority = [(item[0]/ item[1], item[0]) for item in jobs]


    order = sorted(range(len(priority)), key = priority.__getitem__)
    order.reverse()

    return order


def compute_sum(jobs, order):
    time = 0
    weighted_sum = 0

    for i in order:
        time += jobs[i][1]
        weighted_sum += jobs[i][0] * time

    return weighted_sum


def main():
    jobs = read('jobs.txt')
    ordered_jobs = order(jobs, 'ratio')
    weighted_sum = compute_sum(jobs, ordered_jobs)
    print(weighted_sum)


main()

#difference: 69119377652
#ratio: 67311454237
