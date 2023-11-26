# Sales Analysis

#### Install and import necessory libraries


```python
!pip install pandas
!pip install os
!pip install matplotlib


```

    Requirement already satisfied: pandas in c:\users\h\appdata\local\programs\python\python312\lib\site-packages (2.1.3)
    Requirement already satisfied: numpy<2,>=1.26.0 in c:\users\h\appdata\local\programs\python\python312\lib\site-packages (from pandas) (1.26.2)
    Requirement already satisfied: python-dateutil>=2.8.2 in c:\users\h\appdata\local\programs\python\python312\lib\site-packages (from pandas) (2.8.2)
    Requirement already satisfied: pytz>=2020.1 in c:\users\h\appdata\local\programs\python\python312\lib\site-packages (from pandas) (2023.3.post1)
    Requirement already satisfied: tzdata>=2022.1 in c:\users\h\appdata\local\programs\python\python312\lib\site-packages (from pandas) (2023.3)
    Requirement already satisfied: six>=1.5 in c:\users\h\appdata\local\programs\python\python312\lib\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)
    

    
    [notice] A new release of pip is available: 23.2.1 -> 23.3.1
    [notice] To update, run: python.exe -m pip install --upgrade pip
    ERROR: Could not find a version that satisfies the requirement os (from versions: none)
    ERROR: No matching distribution found for os
    
    [notice] A new release of pip is available: 23.2.1 -> 23.3.1
    [notice] To update, run: python.exe -m pip install --upgrade pip
    

    Collecting matplotlib
      Obtaining dependency information for matplotlib from https://files.pythonhosted.org/packages/2e/51/c77a14869b7eb9d6fb440e811b754fc3950d6868c38ace57d0632b674415/matplotlib-3.8.2-cp312-cp312-win_amd64.whl.metadata
      Downloading matplotlib-3.8.2-cp312-cp312-win_amd64.whl.metadata (5.9 kB)
    Collecting contourpy>=1.0.1 (from matplotlib)
      Obtaining dependency information for contourpy>=1.0.1 from https://files.pythonhosted.org/packages/8e/ae/a6353db548bff1a592b85ae6bb80275f0a51dc25a0410d059e5b33183e36/contourpy-1.2.0-cp312-cp312-win_amd64.whl.metadata
      Downloading contourpy-1.2.0-cp312-cp312-win_amd64.whl.metadata (5.8 kB)
    Collecting cycler>=0.10 (from matplotlib)
      Obtaining dependency information for cycler>=0.10 from https://files.pythonhosted.org/packages/e7/05/c19819d5e3d95294a6f5947fb9b9629efb316b96de511b418c53d245aae6/cycler-0.12.1-py3-none-any.whl.metadata
      Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
    Collecting fonttools>=4.22.0 (from matplotlib)
      Obtaining dependency information for fonttools>=4.22.0 from https://files.pythonhosted.org/packages/71/00/46562cbdf644aeaa20666d920e2d6b71a0096ff987ef878ec510e4c1d886/fonttools-4.45.1-cp312-cp312-win_amd64.whl.metadata
      Downloading fonttools-4.45.1-cp312-cp312-win_amd64.whl.metadata (158 kB)
         ---------------------------------------- 0.0/158.4 kB ? eta -:--:--
         ---------------------------------------- 0.0/158.4 kB ? eta -:--:--
         -- ------------------------------------- 10.2/158.4 kB ? eta -:--:--
         ------- ----------------------------- 30.7/158.4 kB 435.7 kB/s eta 0:00:01
         -------------- ---------------------- 61.4/158.4 kB 469.7 kB/s eta 0:00:01
         --------------------- --------------- 92.2/158.4 kB 525.1 kB/s eta 0:00:01
         ---------------------------------- - 153.6/158.4 kB 654.6 kB/s eta 0:00:01
         ------------------------------------ 158.4/158.4 kB 676.3 kB/s eta 0:00:00
    Collecting kiwisolver>=1.3.1 (from matplotlib)
      Obtaining dependency information for kiwisolver>=1.3.1 from https://files.pythonhosted.org/packages/63/50/2746566bdf4a6a842d117367d05c90cfb87ac04e9e2845aa1fa21f071362/kiwisolver-1.4.5-cp312-cp312-win_amd64.whl.metadata
      Downloading kiwisolver-1.4.5-cp312-cp312-win_amd64.whl.metadata (6.5 kB)
    Requirement already satisfied: numpy<2,>=1.21 in c:\users\h\appdata\local\programs\python\python312\lib\site-packages (from matplotlib) (1.26.2)
    Requirement already satisfied: packaging>=20.0 in c:\users\h\appdata\local\programs\python\python312\lib\site-packages (from matplotlib) (23.2)
    Collecting pillow>=8 (from matplotlib)
      Obtaining dependency information for pillow>=8 from https://files.pythonhosted.org/packages/32/e4/978865107d097dd9cb650331676d8dc29ed9fcd0aaab46486e9d6e5123f0/Pillow-10.1.0-cp312-cp312-win_amd64.whl.metadata
      Downloading Pillow-10.1.0-cp312-cp312-win_amd64.whl.metadata (9.6 kB)
    Collecting pyparsing>=2.3.1 (from matplotlib)
      Obtaining dependency information for pyparsing>=2.3.1 from https://files.pythonhosted.org/packages/39/92/8486ede85fcc088f1b3dba4ce92dd29d126fd96b0008ea213167940a2475/pyparsing-3.1.1-py3-none-any.whl.metadata
      Downloading pyparsing-3.1.1-py3-none-any.whl.metadata (5.1 kB)
    Requirement already satisfied: python-dateutil>=2.7 in c:\users\h\appdata\local\programs\python\python312\lib\site-packages (from matplotlib) (2.8.2)
    Requirement already satisfied: six>=1.5 in c:\users\h\appdata\local\programs\python\python312\lib\site-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)
    Downloading matplotlib-3.8.2-cp312-cp312-win_amd64.whl (7.6 MB)
       ---------------------------------------- 0.0/7.6 MB ? eta -:--:--
        --------------------------------------- 0.1/7.6 MB 6.4 MB/s eta 0:00:02
        --------------------------------------- 0.1/7.6 MB 6.4 MB/s eta 0:00:02
       - -------------------------------------- 0.2/7.6 MB 1.9 MB/s eta 0:00:04
       - -------------------------------------- 0.2/7.6 MB 1.9 MB/s eta 0:00:04
       - -------------------------------------- 0.3/7.6 MB 1.4 MB/s eta 0:00:06
       -- ------------------------------------- 0.5/7.6 MB 1.8 MB/s eta 0:00:04
       --- ------------------------------------ 0.6/7.6 MB 1.8 MB/s eta 0:00:04
       --- ------------------------------------ 0.7/7.6 MB 1.8 MB/s eta 0:00:04
       ---- ----------------------------------- 0.8/7.6 MB 1.9 MB/s eta 0:00:04
       ---- ----------------------------------- 0.8/7.6 MB 1.8 MB/s eta 0:00:04
       ---- ----------------------------------- 0.8/7.6 MB 1.8 MB/s eta 0:00:04
       ---- ----------------------------------- 0.8/7.6 MB 1.8 MB/s eta 0:00:04
       ---- ----------------------------------- 0.9/7.6 MB 1.6 MB/s eta 0:00:05
       ---- ----------------------------------- 0.9/7.6 MB 1.6 MB/s eta 0:00:05
       ---- ----------------------------------- 0.9/7.6 MB 1.6 MB/s eta 0:00:05
       ----- ---------------------------------- 1.0/7.6 MB 1.4 MB/s eta 0:00:05
       ----- ---------------------------------- 1.1/7.6 MB 1.4 MB/s eta 0:00:05
       ------ --------------------------------- 1.2/7.6 MB 1.5 MB/s eta 0:00:05
       ------ --------------------------------- 1.3/7.6 MB 1.5 MB/s eta 0:00:05
       ------- -------------------------------- 1.4/7.6 MB 1.5 MB/s eta 0:00:05
       ------- -------------------------------- 1.4/7.6 MB 1.5 MB/s eta 0:00:05
       ------- -------------------------------- 1.4/7.6 MB 1.5 MB/s eta 0:00:05
       ------- -------------------------------- 1.5/7.6 MB 1.4 MB/s eta 0:00:05
       -------- ------------------------------- 1.5/7.6 MB 1.4 MB/s eta 0:00:05
       -------- ------------------------------- 1.7/7.6 MB 1.4 MB/s eta 0:00:05
       --------- ------------------------------ 1.8/7.6 MB 1.5 MB/s eta 0:00:05
       --------- ------------------------------ 1.8/7.6 MB 1.4 MB/s eta 0:00:05
       --------- ------------------------------ 1.8/7.6 MB 1.4 MB/s eta 0:00:05
       --------- ------------------------------ 1.9/7.6 MB 1.4 MB/s eta 0:00:05
       ---------- ----------------------------- 2.0/7.6 MB 1.4 MB/s eta 0:00:04
       ---------- ----------------------------- 2.0/7.6 MB 1.4 MB/s eta 0:00:04
       ---------- ----------------------------- 2.1/7.6 MB 1.4 MB/s eta 0:00:04
       ----------- ---------------------------- 2.1/7.6 MB 1.4 MB/s eta 0:00:04
       ----------- ---------------------------- 2.1/7.6 MB 1.4 MB/s eta 0:00:04
       ----------- ---------------------------- 2.1/7.6 MB 1.4 MB/s eta 0:00:04
       ----------- ---------------------------- 2.1/7.6 MB 1.4 MB/s eta 0:00:04
       ----------- ---------------------------- 2.1/7.6 MB 1.4 MB/s eta 0:00:04
       ----------- ---------------------------- 2.3/7.6 MB 1.3 MB/s eta 0:00:05
       ----------- ---------------------------- 2.3/7.6 MB 1.3 MB/s eta 0:00:05
       ----------- ---------------------------- 2.3/7.6 MB 1.3 MB/s eta 0:00:05
       ------------- -------------------------- 2.6/7.6 MB 1.4 MB/s eta 0:00:04
       ------------- -------------------------- 2.6/7.6 MB 1.4 MB/s eta 0:00:04
       ------------- -------------------------- 2.6/7.6 MB 1.4 MB/s eta 0:00:04
       -------------- ------------------------- 2.7/7.6 MB 1.3 MB/s eta 0:00:04
       -------------- ------------------------- 2.7/7.6 MB 1.3 MB/s eta 0:00:04
       -------------- ------------------------- 2.7/7.6 MB 1.3 MB/s eta 0:00:04
       -------------- ------------------------- 2.8/7.6 MB 1.3 MB/s eta 0:00:04
       --------------- ------------------------ 2.9/7.6 MB 1.3 MB/s eta 0:00:04
       --------------- ------------------------ 3.0/7.6 MB 1.3 MB/s eta 0:00:04
       --------------- ------------------------ 3.0/7.6 MB 1.3 MB/s eta 0:00:04
       --------------- ------------------------ 3.1/7.6 MB 1.3 MB/s eta 0:00:04
       ---------------- ----------------------- 3.1/7.6 MB 1.3 MB/s eta 0:00:04
       ---------------- ----------------------- 3.1/7.6 MB 1.3 MB/s eta 0:00:04
       ---------------- ----------------------- 3.2/7.6 MB 1.3 MB/s eta 0:00:04
       ---------------- ----------------------- 3.2/7.6 MB 1.2 MB/s eta 0:00:04
       ----------------- ---------------------- 3.3/7.6 MB 1.2 MB/s eta 0:00:04
       ----------------- ---------------------- 3.3/7.6 MB 1.2 MB/s eta 0:00:04
       ----------------- ---------------------- 3.3/7.6 MB 1.2 MB/s eta 0:00:04
       ----------------- ---------------------- 3.4/7.6 MB 1.2 MB/s eta 0:00:04
       ----------------- ---------------------- 3.4/7.6 MB 1.2 MB/s eta 0:00:04
       ----------------- ---------------------- 3.4/7.6 MB 1.2 MB/s eta 0:00:04
       ------------------ --------------------- 3.5/7.6 MB 1.2 MB/s eta 0:00:04
       ------------------ --------------------- 3.5/7.6 MB 1.2 MB/s eta 0:00:04
       ------------------ --------------------- 3.5/7.6 MB 1.2 MB/s eta 0:00:04
       ------------------ --------------------- 3.6/7.6 MB 1.2 MB/s eta 0:00:04
       ------------------ --------------------- 3.6/7.6 MB 1.2 MB/s eta 0:00:04
       ------------------- -------------------- 3.6/7.6 MB 1.2 MB/s eta 0:00:04
       ------------------- -------------------- 3.7/7.6 MB 1.2 MB/s eta 0:00:04
       ------------------- -------------------- 3.7/7.6 MB 1.1 MB/s eta 0:00:04
       ------------------- -------------------- 3.7/7.6 MB 1.1 MB/s eta 0:00:04
       ------------------- -------------------- 3.8/7.6 MB 1.1 MB/s eta 0:00:04
       ------------------- -------------------- 3.8/7.6 MB 1.1 MB/s eta 0:00:04
       -------------------- ------------------- 3.9/7.6 MB 1.1 MB/s eta 0:00:04
       -------------------- ------------------- 3.9/7.6 MB 1.1 MB/s eta 0:00:04
       -------------------- ------------------- 3.9/7.6 MB 1.1 MB/s eta 0:00:04
       -------------------- ------------------- 3.9/7.6 MB 1.1 MB/s eta 0:00:04
       -------------------- ------------------- 4.0/7.6 MB 1.1 MB/s eta 0:00:04
       --------------------- ------------------ 4.0/7.6 MB 1.1 MB/s eta 0:00:04
       --------------------- ------------------ 4.0/7.6 MB 1.1 MB/s eta 0:00:04
       --------------------- ------------------ 4.1/7.6 MB 1.1 MB/s eta 0:00:04
       --------------------- ------------------ 4.1/7.6 MB 1.1 MB/s eta 0:00:04
       --------------------- ------------------ 4.1/7.6 MB 1.1 MB/s eta 0:00:04
       --------------------- ------------------ 4.2/7.6 MB 1.1 MB/s eta 0:00:04
       --------------------- ------------------ 4.2/7.6 MB 1.1 MB/s eta 0:00:04
       ---------------------- ----------------- 4.2/7.6 MB 1.1 MB/s eta 0:00:04
       ---------------------- ----------------- 4.3/7.6 MB 1.1 MB/s eta 0:00:04
       ---------------------- ----------------- 4.3/7.6 MB 1.1 MB/s eta 0:00:04
       ---------------------- ----------------- 4.3/7.6 MB 1.0 MB/s eta 0:00:04
       ---------------------- ----------------- 4.4/7.6 MB 1.0 MB/s eta 0:00:04
       ---------------------- ----------------- 4.4/7.6 MB 1.0 MB/s eta 0:00:04
       ----------------------- ---------------- 4.4/7.6 MB 1.0 MB/s eta 0:00:04
       ----------------------- ---------------- 4.5/7.6 MB 1.0 MB/s eta 0:00:04
       ----------------------- ---------------- 4.5/7.6 MB 1.0 MB/s eta 0:00:04
       ----------------------- ---------------- 4.5/7.6 MB 1.0 MB/s eta 0:00:04
       ----------------------- ---------------- 4.6/7.6 MB 1.0 MB/s eta 0:00:03
       ------------------------ --------------- 4.6/7.6 MB 1.0 MB/s eta 0:00:03
       ------------------------ --------------- 4.6/7.6 MB 1.0 MB/s eta 0:00:03
       ------------------------ --------------- 4.6/7.6 MB 1.0 MB/s eta 0:00:04
       ------------------------ --------------- 4.7/7.6 MB 1.0 MB/s eta 0:00:03
       ------------------------ --------------- 4.7/7.6 MB 1.0 MB/s eta 0:00:03
       ------------------------ --------------- 4.8/7.6 MB 1.0 MB/s eta 0:00:03
       ------------------------- -------------- 4.8/7.6 MB 1.0 MB/s eta 0:00:03
       ------------------------- -------------- 4.8/7.6 MB 994.7 kB/s eta 0:00:03
       ------------------------- -------------- 4.8/7.6 MB 994.5 kB/s eta 0:00:03
       ------------------------- -------------- 4.9/7.6 MB 995.6 kB/s eta 0:00:03
       ------------------------- -------------- 4.9/7.6 MB 989.2 kB/s eta 0:00:03
       ------------------------- -------------- 4.9/7.6 MB 990.1 kB/s eta 0:00:03
       -------------------------- ------------- 5.0/7.6 MB 980.9 kB/s eta 0:00:03
       -------------------------- ------------- 5.0/7.6 MB 977.9 kB/s eta 0:00:03
       -------------------------- ------------- 5.0/7.6 MB 981.0 kB/s eta 0:00:03
       -------------------------- ------------- 5.1/7.6 MB 975.0 kB/s eta 0:00:03
       -------------------------- ------------- 5.1/7.6 MB 969.4 kB/s eta 0:00:03
       -------------------------- ------------- 5.2/7.6 MB 973.4 kB/s eta 0:00:03
       --------------------------- ------------ 5.2/7.6 MB 967.7 kB/s eta 0:00:03
       --------------------------- ------------ 5.2/7.6 MB 966.8 kB/s eta 0:00:03
       --------------------------- ------------ 5.3/7.6 MB 967.0 kB/s eta 0:00:03
       --------------------------- ------------ 5.3/7.6 MB 963.3 kB/s eta 0:00:03
       --------------------------- ------------ 5.3/7.6 MB 962.7 kB/s eta 0:00:03
       ---------------------------- ----------- 5.4/7.6 MB 962.0 kB/s eta 0:00:03
       ---------------------------- ----------- 5.4/7.6 MB 959.4 kB/s eta 0:00:03
       ---------------------------- ----------- 5.5/7.6 MB 960.5 kB/s eta 0:00:03
       ---------------------------- ----------- 5.5/7.6 MB 954.3 kB/s eta 0:00:03
       ---------------------------- ----------- 5.5/7.6 MB 951.9 kB/s eta 0:00:03
       ----------------------------- ---------- 5.6/7.6 MB 955.6 kB/s eta 0:00:03
       ----------------------------- ---------- 5.6/7.6 MB 950.6 kB/s eta 0:00:03
       ----------------------------- ---------- 5.6/7.6 MB 951.9 kB/s eta 0:00:03
       ----------------------------- ---------- 5.6/7.6 MB 951.0 kB/s eta 0:00:03
       ----------------------------- ---------- 5.7/7.6 MB 950.6 kB/s eta 0:00:03
       ----------------------------- ---------- 5.7/7.6 MB 949.8 kB/s eta 0:00:03
       ------------------------------ --------- 5.8/7.6 MB 945.2 kB/s eta 0:00:02
       ------------------------------ --------- 5.8/7.6 MB 945.5 kB/s eta 0:00:02
       ------------------------------ --------- 5.8/7.6 MB 943.2 kB/s eta 0:00:02
       ------------------------------ --------- 5.9/7.6 MB 945.1 kB/s eta 0:00:02
       ------------------------------- -------- 5.9/7.6 MB 942.3 kB/s eta 0:00:02
       ------------------------------- -------- 5.9/7.6 MB 940.8 kB/s eta 0:00:02
       ------------------------------- -------- 6.0/7.6 MB 941.9 kB/s eta 0:00:02
       ------------------------------- -------- 6.0/7.6 MB 942.1 kB/s eta 0:00:02
       ------------------------------- -------- 6.1/7.6 MB 939.4 kB/s eta 0:00:02
       -------------------------------- ------- 6.1/7.6 MB 940.5 kB/s eta 0:00:02
       -------------------------------- ------- 6.2/7.6 MB 936.2 kB/s eta 0:00:02
       -------------------------------- ------- 6.2/7.6 MB 939.5 kB/s eta 0:00:02
       -------------------------------- ------- 6.2/7.6 MB 938.2 kB/s eta 0:00:02
       -------------------------------- ------- 6.3/7.6 MB 932.0 kB/s eta 0:00:02
       --------------------------------- ------ 6.3/7.6 MB 932.3 kB/s eta 0:00:02
       --------------------------------- ------ 6.4/7.6 MB 931.3 kB/s eta 0:00:02
       --------------------------------- ------ 6.4/7.6 MB 929.4 kB/s eta 0:00:02
       --------------------------------- ------ 6.5/7.6 MB 928.4 kB/s eta 0:00:02
       ---------------------------------- ----- 6.5/7.6 MB 931.6 kB/s eta 0:00:02
       ---------------------------------- ----- 6.5/7.6 MB 931.2 kB/s eta 0:00:02
       ---------------------------------- ----- 6.6/7.6 MB 929.3 kB/s eta 0:00:02
       ---------------------------------- ----- 6.6/7.6 MB 930.4 kB/s eta 0:00:02
       ---------------------------------- ----- 6.7/7.6 MB 928.7 kB/s eta 0:00:02
       ----------------------------------- ---- 6.7/7.6 MB 931.7 kB/s eta 0:00:02
       ----------------------------------- ---- 6.7/7.6 MB 929.9 kB/s eta 0:00:01
       ----------------------------------- ---- 6.8/7.6 MB 929.0 kB/s eta 0:00:01
       ----------------------------------- ---- 6.8/7.6 MB 930.7 kB/s eta 0:00:01
       ------------------------------------ --- 6.9/7.6 MB 929.6 kB/s eta 0:00:01
       ------------------------------------ --- 6.9/7.6 MB 930.7 kB/s eta 0:00:01
       ------------------------------------ --- 7.0/7.6 MB 928.9 kB/s eta 0:00:01
       ------------------------------------ --- 7.0/7.6 MB 930.0 kB/s eta 0:00:01
       ------------------------------------ --- 7.1/7.6 MB 929.7 kB/s eta 0:00:01
       ------------------------------------- -- 7.1/7.6 MB 928.0 kB/s eta 0:00:01
       ------------------------------------- -- 7.1/7.6 MB 930.3 kB/s eta 0:00:01
       ------------------------------------- -- 7.2/7.6 MB 931.0 kB/s eta 0:00:01
       ------------------------------------- -- 7.2/7.6 MB 929.6 kB/s eta 0:00:01
       -------------------------------------- - 7.3/7.6 MB 929.2 kB/s eta 0:00:01
       -------------------------------------- - 7.3/7.6 MB 928.9 kB/s eta 0:00:01
       -------------------------------------- - 7.4/7.6 MB 931.3 kB/s eta 0:00:01
       -------------------------------------- - 7.4/7.6 MB 929.6 kB/s eta 0:00:01
       -------------------------------------- - 7.4/7.6 MB 929.7 kB/s eta 0:00:01
       ---------------------------------------  7.5/7.6 MB 930.2 kB/s eta 0:00:01
       ---------------------------------------  7.5/7.6 MB 931.7 kB/s eta 0:00:01
       ---------------------------------------  7.6/7.6 MB 929.5 kB/s eta 0:00:01
       ---------------------------------------  7.6/7.6 MB 931.7 kB/s eta 0:00:01
       ---------------------------------------- 7.6/7.6 MB 927.1 kB/s eta 0:00:00
    Downloading contourpy-1.2.0-cp312-cp312-win_amd64.whl (187 kB)
       ---------------------------------------- 0.0/187.7 kB ? eta -:--:--
       -------- ------------------------------ 41.0/187.7 kB 991.0 kB/s eta 0:00:01
       ------------------- -------------------- 92.2/187.7 kB 1.3 MB/s eta 0:00:01
       ------------------------ ------------- 122.9/187.7 kB 901.1 kB/s eta 0:00:01
       ---------------------------------------- 187.7/187.7 kB 1.0 MB/s eta 0:00:00
    Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
    Downloading fonttools-4.45.1-cp312-cp312-win_amd64.whl (2.1 MB)
       ---------------------------------------- 0.0/2.1 MB ? eta -:--:--
       - -------------------------------------- 0.1/2.1 MB 1.7 MB/s eta 0:00:02
       - -------------------------------------- 0.1/2.1 MB 1.3 MB/s eta 0:00:02
       -- ------------------------------------- 0.1/2.1 MB 901.1 kB/s eta 0:00:03
       --- ------------------------------------ 0.2/2.1 MB 1.1 MB/s eta 0:00:02
       ---- ----------------------------------- 0.2/2.1 MB 1.1 MB/s eta 0:00:02
       ----- ---------------------------------- 0.3/2.1 MB 1.0 MB/s eta 0:00:02
       ------ --------------------------------- 0.3/2.1 MB 999.0 kB/s eta 0:00:02
       ------- -------------------------------- 0.4/2.1 MB 1.0 MB/s eta 0:00:02
       ------- -------------------------------- 0.4/2.1 MB 1.0 MB/s eta 0:00:02
       -------- ------------------------------- 0.5/2.1 MB 1.0 MB/s eta 0:00:02
       --------- ------------------------------ 0.5/2.1 MB 994.2 kB/s eta 0:00:02
       ---------- ----------------------------- 0.6/2.1 MB 1.0 MB/s eta 0:00:02
       ----------- ---------------------------- 0.6/2.1 MB 1.0 MB/s eta 0:00:02
       ----------- ---------------------------- 0.6/2.1 MB 976.0 kB/s eta 0:00:02
       ------------ --------------------------- 0.7/2.1 MB 975.9 kB/s eta 0:00:02
       ------------- -------------------------- 0.7/2.1 MB 969.4 kB/s eta 0:00:02
       -------------- ------------------------- 0.8/2.1 MB 996.5 kB/s eta 0:00:02
       --------------- ------------------------ 0.8/2.1 MB 983.9 kB/s eta 0:00:02
       ---------------- ----------------------- 0.9/2.1 MB 989.5 kB/s eta 0:00:02
       ----------------- ---------------------- 0.9/2.1 MB 994.5 kB/s eta 0:00:02
       ------------------ --------------------- 1.0/2.1 MB 988.6 kB/s eta 0:00:02
       ------------------- -------------------- 1.0/2.1 MB 1.0 MB/s eta 0:00:02
       -------------------- ------------------- 1.1/2.1 MB 1.0 MB/s eta 0:00:02
       -------------------- ------------------- 1.1/2.1 MB 992.1 kB/s eta 0:00:02
       ---------------------- ----------------- 1.2/2.1 MB 1.0 MB/s eta 0:00:01
       ---------------------- ----------------- 1.2/2.1 MB 1.0 MB/s eta 0:00:01
       ------------------------ --------------- 1.3/2.1 MB 1.0 MB/s eta 0:00:01
       ------------------------ --------------- 1.3/2.1 MB 1.0 MB/s eta 0:00:01
       ------------------------- -------------- 1.4/2.1 MB 1.0 MB/s eta 0:00:01
       -------------------------- ------------- 1.4/2.1 MB 1.0 MB/s eta 0:00:01
       --------------------------- ------------ 1.5/2.1 MB 1.0 MB/s eta 0:00:01
       ---------------------------- ----------- 1.5/2.1 MB 1.0 MB/s eta 0:00:01
       ----------------------------- ---------- 1.6/2.1 MB 1.0 MB/s eta 0:00:01
       ------------------------------ --------- 1.6/2.1 MB 1.0 MB/s eta 0:00:01
       ------------------------------- -------- 1.7/2.1 MB 1.0 MB/s eta 0:00:01
       -------------------------------- ------- 1.8/2.1 MB 1.0 MB/s eta 0:00:01
       --------------------------------- ------ 1.8/2.1 MB 1.0 MB/s eta 0:00:01
       ---------------------------------- ----- 1.9/2.1 MB 1.0 MB/s eta 0:00:01
       ----------------------------------- ---- 1.9/2.1 MB 1.0 MB/s eta 0:00:01
       ------------------------------------ --- 2.0/2.1 MB 1.1 MB/s eta 0:00:01
       ------------------------------------- -- 2.0/2.1 MB 1.0 MB/s eta 0:00:01
       -------------------------------------- - 2.1/2.1 MB 1.1 MB/s eta 0:00:01
       ---------------------------------------  2.1/2.1 MB 1.1 MB/s eta 0:00:01
       ---------------------------------------- 2.1/2.1 MB 1.1 MB/s eta 0:00:00
    Downloading kiwisolver-1.4.5-cp312-cp312-win_amd64.whl (56 kB)
       ---------------------------------------- 0.0/56.0 kB ? eta -:--:--
       ---------------------------------------- 56.0/56.0 kB 1.5 MB/s eta 0:00:00
    Downloading Pillow-10.1.0-cp312-cp312-win_amd64.whl (2.6 MB)
       ---------------------------------------- 0.0/2.6 MB ? eta -:--:--
        --------------------------------------- 0.1/2.6 MB 1.7 MB/s eta 0:00:02
       - -------------------------------------- 0.1/2.6 MB 1.8 MB/s eta 0:00:02
       -- ------------------------------------- 0.2/2.6 MB 1.1 MB/s eta 0:00:03
       --- ------------------------------------ 0.2/2.6 MB 1.3 MB/s eta 0:00:02
       ---- ----------------------------------- 0.3/2.6 MB 1.4 MB/s eta 0:00:02
       ----- ---------------------------------- 0.4/2.6 MB 1.3 MB/s eta 0:00:02
       ------ --------------------------------- 0.4/2.6 MB 1.3 MB/s eta 0:00:02
       ------ --------------------------------- 0.5/2.6 MB 1.3 MB/s eta 0:00:02
       -------- ------------------------------- 0.5/2.6 MB 1.3 MB/s eta 0:00:02
       --------- ------------------------------ 0.6/2.6 MB 1.4 MB/s eta 0:00:02
       ---------- ----------------------------- 0.7/2.6 MB 1.4 MB/s eta 0:00:02
       ----------- ---------------------------- 0.7/2.6 MB 1.3 MB/s eta 0:00:02
       ------------ --------------------------- 0.8/2.6 MB 1.4 MB/s eta 0:00:02
       ------------ --------------------------- 0.8/2.6 MB 1.3 MB/s eta 0:00:02
       -------------- ------------------------- 0.9/2.6 MB 1.4 MB/s eta 0:00:02
       --------------- ------------------------ 1.0/2.6 MB 1.3 MB/s eta 0:00:02
       --------------- ------------------------ 1.0/2.6 MB 1.3 MB/s eta 0:00:02
       ---------------- ----------------------- 1.1/2.6 MB 1.3 MB/s eta 0:00:02
       ------------------ --------------------- 1.2/2.6 MB 1.4 MB/s eta 0:00:02
       ------------------ --------------------- 1.2/2.6 MB 1.3 MB/s eta 0:00:02
       -------------------- ------------------- 1.3/2.6 MB 1.4 MB/s eta 0:00:01
       --------------------- ------------------ 1.4/2.6 MB 1.4 MB/s eta 0:00:01
       ---------------------- ----------------- 1.5/2.6 MB 1.4 MB/s eta 0:00:01
       ----------------------- ---------------- 1.5/2.6 MB 1.4 MB/s eta 0:00:01
       ------------------------ --------------- 1.6/2.6 MB 1.4 MB/s eta 0:00:01
       ------------------------- -------------- 1.7/2.6 MB 1.4 MB/s eta 0:00:01
       --------------------------- ------------ 1.8/2.6 MB 1.4 MB/s eta 0:00:01
       ---------------------------- ----------- 1.9/2.6 MB 1.5 MB/s eta 0:00:01
       ----------------------------- ---------- 2.0/2.6 MB 1.5 MB/s eta 0:00:01
       ------------------------------- -------- 2.0/2.6 MB 1.5 MB/s eta 0:00:01
       -------------------------------- ------- 2.1/2.6 MB 1.5 MB/s eta 0:00:01
       --------------------------------- ------ 2.2/2.6 MB 1.5 MB/s eta 0:00:01
       ----------------------------------- ---- 2.3/2.6 MB 1.5 MB/s eta 0:00:01
       ------------------------------------ --- 2.4/2.6 MB 1.5 MB/s eta 0:00:01
       ------------------------------------- -- 2.4/2.6 MB 1.5 MB/s eta 0:00:01
       ------------------------------------- -- 2.4/2.6 MB 1.5 MB/s eta 0:00:01
       -------------------------------------- - 2.5/2.6 MB 1.5 MB/s eta 0:00:01
       -------------------------------------- - 2.5/2.6 MB 1.4 MB/s eta 0:00:01
       ---------------------------------------  2.6/2.6 MB 1.5 MB/s eta 0:00:01
       ---------------------------------------- 2.6/2.6 MB 1.4 MB/s eta 0:00:00
    Downloading pyparsing-3.1.1-py3-none-any.whl (103 kB)
       ---------------------------------------- 0.0/103.1 kB ? eta -:--:--
       --------------- ------------------------ 41.0/103.1 kB 1.9 MB/s eta 0:00:01
       ---------------------------------------- 103.1/103.1 kB 1.5 MB/s eta 0:00:00
    Installing collected packages: pyparsing, pillow, kiwisolver, fonttools, cycler, contourpy, matplotlib
    Successfully installed contourpy-1.2.0 cycler-0.12.1 fonttools-4.45.1 kiwisolver-1.4.5 matplotlib-3.8.2 pillow-10.1.0 pyparsing-3.1.1
    

    
    [notice] A new release of pip is available: 23.2.1 -> 23.3.1
    [notice] To update, run: python.exe -m pip install --upgrade pip
    


```python
import pandas as pd
import os
import matplotlib.pyplot as plt
```

#### Importing and Merging all files


```python

folder_path = r"D:\data analyst Course data\Case study\Sales python project\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data"
all_data = pd.DataFrame()


for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        all_data = pd.concat([all_data, df], ignore_index=True)

print(all_data)

        
        
        

```

           Order ID                     Product Quantity Ordered Price Each  \
    0        176558        USB-C Charging Cable                2      11.95   
    1           NaN                         NaN              NaN        NaN   
    2        176559  Bose SoundSport Headphones                1      99.99   
    3        176560                Google Phone                1        600   
    4        176560            Wired Headphones                1      11.99   
    ...         ...                         ...              ...        ...   
    186845   259353      AAA Batteries (4-pack)                3       2.99   
    186846   259354                      iPhone                1        700   
    186847   259355                      iPhone                1        700   
    186848   259356      34in Ultrawide Monitor                1     379.99   
    186849   259357        USB-C Charging Cable                1      11.95   
    
                Order Date                         Purchase Address  
    0       04/19/19 08:46             917 1st St, Dallas, TX 75001  
    1                  NaN                                      NaN  
    2       04/07/19 22:30        682 Chestnut St, Boston, MA 02215  
    3       04/12/19 14:38     669 Spruce St, Los Angeles, CA 90001  
    4       04/12/19 14:38     669 Spruce St, Los Angeles, CA 90001  
    ...                ...                                      ...  
    186845  09/17/19 20:56   840 Highland St, Los Angeles, CA 90001  
    186846  09/01/19 16:00  216 Dogwood St, San Francisco, CA 94016  
    186847  09/23/19 07:39     220 12th St, San Francisco, CA 94016  
    186848  09/19/19 17:30   511 Forest St, San Francisco, CA 94016  
    186849  09/30/19 00:18   250 Meadow St, San Francisco, CA 94016  
    
    [186850 rows x 6 columns]
    

#### Save the file


```python
all_data.to_csv("all_data.csv", index=False)

```


```python
all_data = pd.read_csv("all_data.csv")
all_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order ID</th>
      <th>Product</th>
      <th>Quantity Ordered</th>
      <th>Price Each</th>
      <th>Order Date</th>
      <th>Purchase Address</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>176558</td>
      <td>USB-C Charging Cable</td>
      <td>2</td>
      <td>11.95</td>
      <td>04/19/19 08:46</td>
      <td>917 1st St, Dallas, TX 75001</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>176559</td>
      <td>Bose SoundSport Headphones</td>
      <td>1</td>
      <td>99.99</td>
      <td>04/07/19 22:30</td>
      <td>682 Chestnut St, Boston, MA 02215</td>
    </tr>
    <tr>
      <th>3</th>
      <td>176560</td>
      <td>Google Phone</td>
      <td>1</td>
      <td>600</td>
      <td>04/12/19 14:38</td>
      <td>669 Spruce St, Los Angeles, CA 90001</td>
    </tr>
    <tr>
      <th>4</th>
      <td>176560</td>
      <td>Wired Headphones</td>
      <td>1</td>
      <td>11.99</td>
      <td>04/12/19 14:38</td>
      <td>669 Spruce St, Los Angeles, CA 90001</td>
    </tr>
  </tbody>
</table>
</div>



#### Clean up the Data


```python
# when we merge all the files the headers of all the files are also duplicated
temp_df = all_data[all_data['Order ID'].str[0:5] == 'Order']
temp_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order ID</th>
      <th>Product</th>
      <th>Quantity Ordered</th>
      <th>Price Each</th>
      <th>Order Date</th>
      <th>Purchase Address</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>519</th>
      <td>Order ID</td>
      <td>Product</td>
      <td>Quantity Ordered</td>
      <td>Price Each</td>
      <td>Order Date</td>
      <td>Purchase Address</td>
    </tr>
    <tr>
      <th>1149</th>
      <td>Order ID</td>
      <td>Product</td>
      <td>Quantity Ordered</td>
      <td>Price Each</td>
      <td>Order Date</td>
      <td>Purchase Address</td>
    </tr>
    <tr>
      <th>1155</th>
      <td>Order ID</td>
      <td>Product</td>
      <td>Quantity Ordered</td>
      <td>Price Each</td>
      <td>Order Date</td>
      <td>Purchase Address</td>
    </tr>
    <tr>
      <th>2878</th>
      <td>Order ID</td>
      <td>Product</td>
      <td>Quantity Ordered</td>
      <td>Price Each</td>
      <td>Order Date</td>
      <td>Purchase Address</td>
    </tr>
    <tr>
      <th>2893</th>
      <td>Order ID</td>
      <td>Product</td>
      <td>Quantity Ordered</td>
      <td>Price Each</td>
      <td>Order Date</td>
      <td>Purchase Address</td>
    </tr>
  </tbody>
</table>
</div>




```python
# We have to drop all the duplicated rows
all_data = all_data[all_data['Order ID'].str[0:5] != 'Order']
```


```python
# check for null values
na_df = all_data[all_data.isna().any(axis=1)]
na_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order ID</th>
      <th>Product</th>
      <th>Quantity Ordered</th>
      <th>Price Each</th>
      <th>Order Date</th>
      <th>Purchase Address</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>356</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>735</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1433</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1553</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Drop nulls
all_data = all_data.dropna(how='all')
```

#### Create new 'month' column


```python
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data ['Month'] = all_data['Month'].astype('int')
all_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order ID</th>
      <th>Product</th>
      <th>Quantity Ordered</th>
      <th>Price Each</th>
      <th>Order Date</th>
      <th>Purchase Address</th>
      <th>Month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>176558</td>
      <td>USB-C Charging Cable</td>
      <td>2</td>
      <td>11.95</td>
      <td>04/19/19 08:46</td>
      <td>917 1st St, Dallas, TX 75001</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>176559</td>
      <td>Bose SoundSport Headphones</td>
      <td>1</td>
      <td>99.99</td>
      <td>04/07/19 22:30</td>
      <td>682 Chestnut St, Boston, MA 02215</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>176560</td>
      <td>Google Phone</td>
      <td>1</td>
      <td>600</td>
      <td>04/12/19 14:38</td>
      <td>669 Spruce St, Los Angeles, CA 90001</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>176560</td>
      <td>Wired Headphones</td>
      <td>1</td>
      <td>11.99</td>
      <td>04/12/19 14:38</td>
      <td>669 Spruce St, Los Angeles, CA 90001</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>176561</td>
      <td>Wired Headphones</td>
      <td>1</td>
      <td>11.99</td>
      <td>04/30/19 09:27</td>
      <td>333 8th St, Los Angeles, CA 90001</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



#### Make a Sales column


```python
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'], errors='coerce')

all_data['Price Each'] = pd.to_numeric(all_data['Price Each'], errors='coerce')
all_data['Sales'] = all_data['Quantity Ordered']*all_data['Price Each']
print(all_data.head())
```

      Order ID                     Product  Quantity Ordered  Price Each  \
    0   176558        USB-C Charging Cable                 2       11.95   
    2   176559  Bose SoundSport Headphones                 1       99.99   
    3   176560                Google Phone                 1      600.00   
    4   176560            Wired Headphones                 1       11.99   
    5   176561            Wired Headphones                 1       11.99   
    
           Order Date                      Purchase Address  Month   Sales  
    0  04/19/19 08:46          917 1st St, Dallas, TX 75001      4   23.90  
    2  04/07/19 22:30     682 Chestnut St, Boston, MA 02215      4   99.99  
    3  04/12/19 14:38  669 Spruce St, Los Angeles, CA 90001      4  600.00  
    4  04/12/19 14:38  669 Spruce St, Los Angeles, CA 90001      4   11.99  
    5  04/30/19 09:27     333 8th St, Los Angeles, CA 90001      4   11.99  
    

#### Create a City column


```python
all_data['City'] = all_data['Purchase Address'].apply(lambda x: f"{x.split(', ')[1]}, {x.split(', ')[2].split(' ')[0]}")

all_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order ID</th>
      <th>Product</th>
      <th>Quantity Ordered</th>
      <th>Price Each</th>
      <th>Order Date</th>
      <th>Purchase Address</th>
      <th>Month</th>
      <th>Sales</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>176558</td>
      <td>USB-C Charging Cable</td>
      <td>2</td>
      <td>11.95</td>
      <td>04/19/19 08:46</td>
      <td>917 1st St, Dallas, TX 75001</td>
      <td>4</td>
      <td>23.90</td>
      <td>Dallas, TX</td>
    </tr>
    <tr>
      <th>2</th>
      <td>176559</td>
      <td>Bose SoundSport Headphones</td>
      <td>1</td>
      <td>99.99</td>
      <td>04/07/19 22:30</td>
      <td>682 Chestnut St, Boston, MA 02215</td>
      <td>4</td>
      <td>99.99</td>
      <td>Boston, MA</td>
    </tr>
    <tr>
      <th>3</th>
      <td>176560</td>
      <td>Google Phone</td>
      <td>1</td>
      <td>600.00</td>
      <td>04/12/19 14:38</td>
      <td>669 Spruce St, Los Angeles, CA 90001</td>
      <td>4</td>
      <td>600.00</td>
      <td>Los Angeles, CA</td>
    </tr>
    <tr>
      <th>4</th>
      <td>176560</td>
      <td>Wired Headphones</td>
      <td>1</td>
      <td>11.99</td>
      <td>04/12/19 14:38</td>
      <td>669 Spruce St, Los Angeles, CA 90001</td>
      <td>4</td>
      <td>11.99</td>
      <td>Los Angeles, CA</td>
    </tr>
    <tr>
      <th>5</th>
      <td>176561</td>
      <td>Wired Headphones</td>
      <td>1</td>
      <td>11.99</td>
      <td>04/30/19 09:27</td>
      <td>333 8th St, Los Angeles, CA 90001</td>
      <td>4</td>
      <td>11.99</td>
      <td>Los Angeles, CA</td>
    </tr>
  </tbody>
</table>
</div>



#### What are the monthly Sales 


```python
monthly_sales = all_data.groupby('Month').agg({
    'Quantity Ordered': 'sum',
    'Price Each': 'sum',
    'Sales': 'sum'
}).reset_index()
monthly_sales = monthly_sales.sort_values(by='Sales', ascending=False)

print(monthly_sales)
```

        Month  Quantity Ordered  Price Each       Sales
    11     12             28114  4588415.41  4613443.34
    9      10             22703  3715554.83  3736726.88
    3       4             20558  3367671.02  3390670.24
    10     11             19798  3180600.68  3199603.20
    4       5             18667  3135125.13  3152606.75
    2       3             17005  2791207.83  2807100.38
    6       7             16072  2632539.56  2647775.76
    5       6             15253  2562025.61  2577802.26
    7       8             13448  2230345.42  2244467.88
    1       2             13449  2188884.72  2202022.42
    8       9             13109  2084992.09  2097560.13
    0       1             10903  1811768.38  1822256.73
    


```python
plt.bar(monthly_sales['Month'], monthly_sales['Sales'])
plt.xticks(monthly_sales['Month'])
plt.xlabel('Months')
plt.ylabel('Total Sales')
plt.show()
```


    
![png](output_22_0.png)
    


#### December month have most sales and January has the slowest sales recorded

#### Sales according to cities


```python
city_sales = all_data.groupby('City').agg({
    'Quantity Ordered': 'sum',
    'Price Each': 'sum',
    'Sales': 'sum'
}).reset_index()
city_sales = city_sales.sort_values(by='Sales', ascending=False)

print(city_sales)
```

                    City  Quantity Ordered  Price Each       Sales
    8  San Francisco, CA             50239  8211461.74  8262203.91
    4    Los Angeles, CA             33289  5421435.23  5452570.80
    5  New York City, NY             27932  4635370.83  4664317.43
    2         Boston, MA             22528  3637409.77  3661642.01
    0        Atlanta, GA             16602  2779908.20  2795498.58
    3         Dallas, TX             16730  2752627.82  2767975.40
    9        Seattle, WA             16553  2733296.01  2747755.48
    7       Portland, OR             11303  1860558.22  1870732.34
    1         Austin, TX             11153  1809873.61  1819581.75
    6       Portland, ME              2750   447189.25   449758.27
    


```python
plt.bar(city_sales['City'], city_sales['Sales'])
plt.xticks(city_sales['City'], rotation= 'vertical', size= 8)
plt.xlabel('Cities Names')
plt.ylabel('Total Sales')
plt.show()
```


    
![png](output_26_0.png)
    


#### San Francisco, CA has the highest sales recorded and Portland, ME has the least sales record.

#### What time customers buy the most


```python
# First we have to convert Order Date column into datetime data type
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'], format='%m/%d/%y %H:%M')

```


```python
# Convert 'Order Date' column to datetime type
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])

# Extract hour from 'Order Date' and create a new column 'Hour'
all_data['Hour'] = all_data['Order Date'].dt.hour

# Group data by 'Hour' and sum the 'Sales' for each hour
hourly_sales = all_data.groupby('Hour')['Sales'].sum()

# Create a line chart
plt.figure(figsize=(12, 6))
plt.plot(hourly_sales.index, hourly_sales.values, marker='o', linestyle='-', color='b')
plt.title('Total Sales Over Time (Hourly)')
plt.xlabel('Hour of the Day')
plt.ylabel('Total Sales')
plt.grid(True)
plt.xticks(range(24))  

# Show the plot
plt.show()



    
```


    
![png](output_30_0.png)
    


#### 11 AM to 7 PM is the peak time

#### What products are most sold?


```python


product_sales = all_data.groupby('Product')['Quantity Ordered'].sum()


product_sales = product_sales.sort_values(ascending=False)
product_sales.head()

```




    Product
    AAA Batteries (4-pack)      31017
    AA Batteries (4-pack)       27635
    USB-C Charging Cable        23975
    Lightning Charging Cable    23217
    Wired Headphones            20557
    Name: Quantity Ordered, dtype: int64




```python
# Create a bar chart
plt.figure(figsize=(12, 6))


product_sales.plot(kind='bar', color='skyblue')


plt.title('Total Quantity Sold by Product')
plt.xlabel('Product')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=90)


plt.show()

```


    
![png](output_34_0.png)
    


#### AAA Batteries are the most sold product and LG Dryer is the least sold product

#### Products sold in respect to their prices


```python


product_data = all_data.groupby('Product').agg({'Quantity Ordered': 'sum', 'Price Each': 'mean'})

product_data = product_data.sort_values(by='Quantity Ordered', ascending=False)

product_data.head(20)


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Quantity Ordered</th>
      <th>Price Each</th>
    </tr>
    <tr>
      <th>Product</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AAA Batteries (4-pack)</th>
      <td>31017</td>
      <td>2.99</td>
    </tr>
    <tr>
      <th>AA Batteries (4-pack)</th>
      <td>27635</td>
      <td>3.84</td>
    </tr>
    <tr>
      <th>USB-C Charging Cable</th>
      <td>23975</td>
      <td>11.95</td>
    </tr>
    <tr>
      <th>Lightning Charging Cable</th>
      <td>23217</td>
      <td>14.95</td>
    </tr>
    <tr>
      <th>Wired Headphones</th>
      <td>20557</td>
      <td>11.99</td>
    </tr>
    <tr>
      <th>Apple Airpods Headphones</th>
      <td>15661</td>
      <td>150.00</td>
    </tr>
    <tr>
      <th>Bose SoundSport Headphones</th>
      <td>13457</td>
      <td>99.99</td>
    </tr>
    <tr>
      <th>27in FHD Monitor</th>
      <td>7550</td>
      <td>149.99</td>
    </tr>
    <tr>
      <th>iPhone</th>
      <td>6849</td>
      <td>700.00</td>
    </tr>
    <tr>
      <th>27in 4K Gaming Monitor</th>
      <td>6244</td>
      <td>389.99</td>
    </tr>
    <tr>
      <th>34in Ultrawide Monitor</th>
      <td>6199</td>
      <td>379.99</td>
    </tr>
    <tr>
      <th>Google Phone</th>
      <td>5532</td>
      <td>600.00</td>
    </tr>
    <tr>
      <th>Flatscreen TV</th>
      <td>4819</td>
      <td>300.00</td>
    </tr>
    <tr>
      <th>Macbook Pro Laptop</th>
      <td>4728</td>
      <td>1700.00</td>
    </tr>
    <tr>
      <th>ThinkPad Laptop</th>
      <td>4130</td>
      <td>999.99</td>
    </tr>
    <tr>
      <th>20in Monitor</th>
      <td>4129</td>
      <td>109.99</td>
    </tr>
    <tr>
      <th>Vareebadd Phone</th>
      <td>2068</td>
      <td>400.00</td>
    </tr>
    <tr>
      <th>LG Washing Machine</th>
      <td>666</td>
      <td>600.00</td>
    </tr>
    <tr>
      <th>LG Dryer</th>
      <td>646</td>
      <td>600.00</td>
    </tr>
  </tbody>
</table>
</div>




```python

fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.bar(product_data.index, product_data['Quantity Ordered'], color='skyblue', label='Quantity Sold')
ax1.set_xlabel('Product')
ax1.set_ylabel('Quantity Sold', color='skyblue')
ax1.tick_params('y', colors='skyblue')

ax1.set_xticks(range(len(product_data.index)))
ax1.set_xticklabels(product_data.index, rotation=90, ha='center')

ax2 = ax1.twinx()
ax2.plot(product_data.index, product_data['Price Each'], color='orange', label='Price')
ax2.set_ylabel('Price', color='orange')
ax2.tick_params('y', colors='orange')

plt.title('Product Sales and Prices')
fig.tight_layout()
plt.show()

```


    
![png](output_38_0.png)
    


#### Lowest the price, higher the selling. LG Dryer has a high price and low selling.
