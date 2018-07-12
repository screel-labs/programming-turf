#include<stdlib.h>
#include<stdio.h>

int cmf(void const *a,void const *b){
	return (*(int*)a - *(int*)b);
}

int main(){
	int t;
	scanf("%d",&t);
	while(t--){
		int n,x;
		scanf("%d %d",&n,&x);
		int a[n+1],i,j,count=0,ele;
		for(i=0;i<n;i++) scanf("%d",&a[i]);
		qsort(a,n,sizeof(int),cmf);
		i=0,j=n-1;
		int *ele_pos;
		while(i<j){
			ele=x-a[i];
			//printf("Search element%d\n",ele);
			ele_pos=(int*)bsearch(&ele,a+i,j-i+1,sizeof(int),cmf);
			if(ele_pos!=NULL){
				j=*ele_pos-1;
				//printf("Search element Position%d\n",j);
				//printf("%d %d\n",a[i],a[j]);
				count++;
			}
			i++;
		}
		if(count) printf("Yes\n");
		else printf("No\n");
	}
	return 0;
}
