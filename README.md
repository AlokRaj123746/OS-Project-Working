🚀 Advanced Disk Scheduling Simulator
An interactive Streamlit-based web application that visualizes and compares classical Disk Scheduling Algorithms.
It helps users understand how different algorithms minimize seek time and impact system performance using animations, charts, and performance metrics.

⭐Supported Algorithm:
Algorithm	                                       Description
FCFS (First Come First Serve)	                   Processes requests in arrival order
SSTF (Shortest Seek Time First)	                 Selects the request closest to current head
SCAN (Elevator Algorithm)	                       Moves in left/right direction serving requests                                                     and then reverses
C-SCAN (Circular SCAN)	                         Moves in Clockwise/AntiClockwise direction, jumps                                                  to beginning of disk, and continues

🎯Key Features
User-defined disk request queue
✔ Select starting head position
✔ Select SCAN / C-SCAN direction (left or right)
✔ Adjustable animation speed
✔ Random request generator
✔ Performance calculations:
  Total Seek Time
  Average Seek Time
  Throughput
✔ Visualizations:
  Disk head movement animation
  Line plot for movement pattern
  Bar chart for algorithm comparison
✔ Export results to CSV file

🖥️ LIVE DEMO
Hosted on Streamlit Cloud:

Anyone can access the project online — no installation required.
🛠️ Tech Stack
Component	                          Technology
Frontend UI	                         Streamlit
Visualization	                       Plotly
Data Handling	                       Pandas, NumPy
Programming Language	               Python
Deployment	                         Streamlit Cloud

🧠 Working of Project

1️⃣ User enters disk requests
2️⃣ Selects head starting position & algorithm
3️⃣ For SCAN/C-SCAN, select direction (left/right)
4️⃣ App computes:
  Head movement order
  Total & average seek time
  Throughput
5️⃣ Animations and charts display results visually

📊 Performance Comparison
Algorithm	  Total Seek Time	  Avg Seek Time	    Throughput
FCFS	        High	            Moderate	        Low
SSTF	        Low	              Low	              Medium
SCAN	        Medium	          Medium	          Medium
C-SCAN	      Medium	          High	            High

📌 Performance varies based on request distribution and head position.

🚀 Future Enhancements
🔹 Add more UI customization themes
🔹 Include real-time I/O request simulation

⭐Conclusion
The Advanced Disk Scheduling Simulator effectively visualizes how different disk scheduling algorithms manage I/O requests. By allowing users to input custom requests and compare FCFS, SSTF, SCAN, and C-SCAN, the project clearly shows how each algorithm affects seek time, average delay, and throughput. The simulator proves that FCFS is simple but inefficient, SSTF improves performance but may starve requests, and SCAN/C-SCAN provide balanced and fair access patterns for larger workloads. Overall, the project successfully converts theoretical OS concepts into an interactive and practical learning tool, helping users understand how scheduling decisions impact disk performance.
