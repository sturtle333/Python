#include <stdio.h>
#include <iostream>

using namespace std;

typedef struct Number {
	int value;
	int arr;
};

void quickSort(Number *array, int low, int high);

int main() {
	int N;
	scanf("%d", &N);
	Number numN[N];
	for(int a=0;a<N;a++){
		cin>>numN[a].value;
		numN[a].arr = a+1;
	}
	int M;
	scanf("%d", &M);
	Number numM[M];
	for(int a=0;a<M;a++){
		cin>>numM[a].value;
		numM[a].arr = a+1;
	}
	int Q[M];
	
	quickSort(numN,0,N);
	quickSort(numM,0,M);
	
	for (int Ma=0,Nb=0;Ma<M;){
		if(numM[Ma].value==numN[Nb].value) {
			Q[Ma++] = numN[Nb++].arr;
		}
		else if (numM[Ma].value<numN[Nb].value){
			Q[Ma++] = -1;
			Nb++;
		}
		else if (numM[Ma].value>numM[Nb].value){
			Nb++;
		}
	}
	
	for(int a=0;a<M;a++){
		printf("%d ",Q[a]);
	}
	return 0;
}

void quickSort(Number *array, int low, int high)
{
    int i = low;
    int j = high;
    int pivot = array[(i + j) / 2].value;
    Number temp;

    while (i <= j)
    {
        while (array[i].value < pivot)
            i++;
        while (array[j].value > pivot)
            j--;
        if (i <= j) {
            temp = array[i];
            array[i] = array[j];
            array[j] = temp;
            i++;
            j--;
        }
    }
    if (j > low)
        quickSort(array, low, j);
    if (i < high)
        quickSort(array, i, high);
}

/*
in:
5
23 5 32 87 50
4
5 2 100 87

out:
2 -1 -1 4
*/ 
