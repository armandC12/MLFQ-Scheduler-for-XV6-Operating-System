# MLFQ Process Scheduler

This project implements a Multilevel Feedback Queue (MLFQ) process scheduler in the XV6 operating system. The MLFQ scheduler aims to improve the distribution of processor time among processes by dynamically adjusting their priorities based on their behavior.

## What is MLFQ?

The Multilevel Feedback Queue scheduling algorithm is a variation of the round-robin scheduling algorithm that assigns different priority levels to processes. Each level has a different time quantum, and processes are promoted or demoted between levels based on their CPU usage. This allows the scheduler to give higher priority to interactive or I/O-bound processes and lower priority to CPU-bound processes.

## Implementation Details

In this project, the original scheduler in XV6 is replaced with an MLFQ scheduler. The scheduler selects the next process to run based on their priority levels and uses round-robin scheduling within each level. The priority of a process is adjusted according to the following rules:

- Rule 1: If process A has a higher priority than process B, process A is chosen to run.
- Rule 2: If two processes have the same priority, they run in a round-robin fashion within their priority level.
- Rule 3: When a process starts, its priority is set to the highest level.
- Rule 4: A process's priority decreases after completing a full quantum of CPU computation.
- Rule 5 (Extra): Implement priority boost to periodically raise the priority of all processes to prevent starvation.

The project includes measurement experiments using user-level programs, "iobench" and "cpubench," to observe the effects of the MLFQ scheduler on I/O-bound and CPU-bound processes.

## Instructions

To run the MLFQ scheduler implementation in XV6, follow these steps:

1. Clone the XV6 repository: `git clone https://github.com/mit-pdos/xv6-riscv.git`
2. Switch to the xv6 directory: `cd xv6`
3. Apply the MLFQ scheduler patch.
4. Build the XV6 kernel: `make`
5. Run XV6 in the QEMU emulator: `make qemu`

Refer to the lab report for a detailed analysis of the MLFQ scheduler's performance and additional optional tasks.

**Note:** Make sure to follow the XV6 coding style and conventions when making modifications.

For more information on XV6 and the MLFQ scheduler, please refer to the lab report included in this repository.
