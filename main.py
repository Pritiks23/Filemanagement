from scheduler import Task, shortest_job_first

def print_results(tasks, gantt_chart):
    print("\nTask\tArrival\tBurst\tWaiting\tTurnaround")
    for t in tasks:
        print(f"{t.pid}\t{t.arrival_time}\t{t.burst_time}\t{t.waiting_time}\t{t.turnaround_time}")
    
    print("\nGantt Chart:")
    prev = 0
    for pid, end_time in gantt_chart:
        print(f"| {pid} ({prev}→{end_time}) ", end="")
        prev = end_time
    print("|")

if __name__ == "__main__":
    task_list = [
        Task("P1", 0, 8),
        Task("P2", 1, 4),
        Task("P3", 2, 9),
        Task("P4", 3, 5),
    ]
    scheduled_tasks, gantt = shortest_job_first(task_list)
    print_results(scheduled_tasks, gantt)
