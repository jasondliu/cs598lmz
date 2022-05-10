import ctypes
ctypes.cast( <address>, ctypes.POINTER(ctypes.c_ubyte) )[0]

The first element in the array has offset ctypes.sizeof(ctypes.c_long)
*/
#include<stdio.h>

#include<stdlib.h>
#include <time.h>


void main()
{
	FILE *fp;
	clock_t	start,stop;
	double s;
	int n=10000000;
	start=clock();
	fp=fopen("myfirstfile1.txt","w");
	for(int i=0;i<n;i++)
	{
		fprintf(fp,"Hello bro!\n");
	}
	fclose(fp);
	stop=clock();
	s=(double)(stop-start)/CLOCKS_PER_SEC;
	//printf("1.darti hae=%lld\n",stop-start);
	printf("1. time by fprintf=%lf\n",s);
	start=clock();
	fp=fopen("myfirstfile
