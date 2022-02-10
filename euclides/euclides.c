#include<stdio.h>
#include<stdlib.h>

int gcd(int, int);

int main(void){
    int a=0;
    int b=0;
    while(a!=10){
        printf("\nEscribe un valor para a: ");
        scanf("%i", &a);
        printf("\nEscribe un valor para b: ");
        scanf("%i", &b);
        printf("\nEl Maximo comun divisor de %i, %i es: %i", a,b,gcd(a,b));
    }
}

int gcd(int a, int n){
    int u=a, v=n, x1=1, q, r=1, x, x2=0;
    while(u!=1 && u!=0){
        q=(v/u);
        r=v-(q*u);
        x=x2-(q*x1);
        v=u;
        u=r;
        x2=x1;
        x1=x;
    }
    return (r);
}

int ** llaveHill(int n){
    srand( (unsigned)time( NULL ) );
    int **K;
    int x=1;
    do{
        for(int i=0; i<3;i++){
            for(int j=0; j<3;j++){
                *(*(K+i)+j)=rand()%n;
            }
        }
        x=determinante(K);
    }while(x==0||gcd(x,n)!=1);

	return K
}

int determinante(int K[3][3]){
    int x;

	x=(K[0][0]*K[1][1]*K[2][2]+K[1][0]*K[2][1]*K[0][2]+
    K[2][0]*K[0][1]*K[1][2]-(K[0][2]*K[1][1]*K[2][0])-
    (K[1][2]*K[2][1]*K[0][0])-(K[2][2]*K[1][0]*K[0][1]));
	
    return x;
}

