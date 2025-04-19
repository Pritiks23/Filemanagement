class Task:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.completed = False

def shortest_job_first(tasks):
    time = 0
    completed_tasks = 0
    n = len(tasks)
    gantt_chart = []

    while completed_tasks < n:
        available_tasks = [t for t in tasks if t.arrival_time <= time and not t.completed]
        if available_tasks:
            current = min(available_tasks, key=lambda t: t.burst_time)
            current.waiting_time = time - current.arrival_time
            time += current.burst_time
            current.turnaround_time = time - current.arrival_time
            current.completed = True
            gantt_chart.append((current.pid, time))
            completed_tasks += 1
        else:
            time += 1

    return tasks, gantt_chart
