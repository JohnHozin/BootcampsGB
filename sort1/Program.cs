// сортировка подсчётом
//int[] array = { 10, int.MaxValue, 9, 8, 39, 3, 15 };
//Console.WriteLine("[" + string.Join(", ", array) + "]");
//CountingSort(array);
//CountingSortExtended(array);

// сортировка параллельная
const int THREADS_NUMBERS = 8; // число потоков
const int N = 1000000; //размер массива
object locker = new object();

Random rand = new Random();
int[] resSerial = new int[N].Select(r => rand.Next(0, 5)).ToArray();
int[] resParalel = new int[N];
Array.Copy(resSerial, resParalel, N);

CountingSortExtended(resSerial);
PrepareParallelCoutingSort(resParalel);
Console.WriteLine(EqualityMatrix(resSerial, resParalel));

//Console.WriteLine("1.[" + string.Join(", ", resSerial) + "]");
//Console.WriteLine("2.[" + string.Join(", ", resParalel) + "]");

void PrepareParallelCoutingSort(int[] inputArray)
{
    int max = inputArray.Max();
    int min = inputArray.Min();

    int offset = -min;
    int[] counters = new int[max + offset + 1];

    int eachThreadCalc = N / THREADS_NUMBERS;
    var threadParall = new List<Thread>();

    for (int i = 0; i < THREADS_NUMBERS; i++)
    {
        int startPos = i * eachThreadCalc;
        int endPos = (i + 1) * eachThreadCalc;
        if (i == THREADS_NUMBERS - 1) endPos = N;
        threadParall.Add(new Thread(() => CountingSortParallel(inputArray, counters, offset, startPos, endPos)));
        threadParall[i].Start();
    }

    foreach (var thread in threadParall)
    {
        thread.Join();
    }

    int index = 0;
    for (int i = 0; i < counters.Length; i++)
    {
        for (int k = 0; k < counters[i]; k++)
        {
            inputArray[index] = i - offset;
            index++;
        }
    }
}

void CountingSortParallel(int[] inputArray, int[] counters, int offset, int startPos, int endPos)
{
    for (int i = startPos; i < endPos; i++)
    {
        lock (locker)
        {
            counters[inputArray[i] + offset]++;
        }
    }
}

bool EqualityMatrix(int[] fmatrix, int[] smatrix)
{
    bool res = true;
    for (int i = 0; i < N; i++)
    {
        res = res && (fmatrix[i] == smatrix[i]);
    }

    return res;
}


void CountingSort(int[] inputArray)
{
    int[] counters = new int[10];

    for (int i = 0; i < inputArray.Length; i++)
    {
        counters[inputArray[i]]++;
    }
    int j = 0;
    for (int i = 0; i < counters.Length; i++)
    {
        // while(counters[i]>0)
        // {
        //     inputArray[j] = i;
        //     j++;
        //     counters[i]--;
        // }    

        for (int k = 0; k < counters[i]; k++)
        {
            inputArray[j] = i;
            j++;
        }
    }
    Console.WriteLine("[" + string.Join(", ", inputArray) + "]");
}

void CountingSortExtended(int[] inputArray)
{
    int max = inputArray.Max();
    int min = inputArray.Min();

    int offset = -min;

    int[] counters = new int[max + offset + 1];
    for (int i = 0; i < inputArray.Length; i++)
    {
        counters[inputArray[i] + offset]++;
    }
    int j = 0;
    for (int i = 0; i < counters.Length; i++)
    {
        for (int k = 0; k < counters[i]; k++)
        {
            inputArray[j] = i - offset;
            j++;
        }
    }
    //Console.WriteLine("[" + string.Join(", ", inputArray) + "]");
}



