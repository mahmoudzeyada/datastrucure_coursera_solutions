# python3
'''optimized code using heapq module'''
import heapq
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class Worker:
    __slots__ = ['id', 'priority']

    def __init__(self, id, priority):
        self.id = id
        self.priority = priority

    def __lt__(self, child_worker):
        if child_worker.priority == self.priority:
            return self.id < child_worker.id
        return self.priority < child_worker.priority

    def __gt__(self, child_worker):
        if child_worker.priority == self.priority:
            return self.id > child_worker.id
        return self.priority > child_worker.priority


def assign_jobs(n_workers, jobs):
    workers = [Worker(i, 0) for i in range(n_workers)]
    results = []
    append = results.append

    for job in jobs:
        next_worker = workers[0]
        results.append(AssignedJob(next_worker.id, next_worker.priority))
        next_worker.priority += job
        heapq.heapreplace(workers, next_worker)
    return results


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


main()
''' this my code '''


# from collections import namedtuple

# AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


# class WorkerPriority:
#     __slots__ = ['worker', 'priority']

#     def __init__(self, worker, priority):
#         self.worker = worker
#         self.priority = priority


# def parent(i):
#     return int((i-1)/2)


# def left(i):
#     return (2*i)+1


# def right(i):
#     return (2*i)+2


# def compare_workers(worker1, worker2):
#     if worker1.priority == worker2.priority:
#         return worker1.worker > worker2.worker
#     return worker1.priority > worker2.priority


# def heapify(a, i):
#     ''' function for mantaing max heap property time-complexity = O(log n) but that it is that is optimized version  '''
#     l = left(i)
#     r = right(i)
#     smallest = i

#     if l < len(a) and compare_workers(a[i], a[l]):
#         smallest = l

#     if r < len(a) and compare_workers(a[smallest], a[r]):
#         smallest = r

#     if smallest != i:
#         a[i], a[smallest] = a[smallest], a[i]
#         heapify(a, smallest)
#     return a


# def increase_root_key_heap(heap, key):
#     ''' function for increasing min heap binary tree time-complexity = O(log(n)) '''
#     heap[0].priority += key
#     return heapify(heap, 0)


# def assign_jobs(n_workers, jobs):
#     workers = [WorkerPriority(i, 0) for i in range(n_workers)]
#     results = []
#     append = results.append

#     for job in jobs:
#         next_worker = workers[0]
#         results.append(AssignedJob(next_worker.worker, next_worker.priority))
#         increase_root_key_heap(workers, job)
#     return results


# def main():
#     n_workers, n_jobs = map(int, input().split())
#     jobs = list(map(int, input().split()))
#     assert len(jobs) == n_jobs

#     assigned_jobs = assign_jobs(n_workers, jobs)

#     for job in assigned_jobs:
#         print(job.worker, job.started_at)
