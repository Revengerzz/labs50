#include <stdio.h>
#include <math.h>

int main(void)
{
float a,x,g,y,f,bukva;
double pi = 3.1415926;
printf("Введите х ");
scanf("%f", &x);
printf("Введите a ");
scanf("%f", &a);
printf("Что считаем? ");
scanf("%f", &bukva);
if (bukva==1){
    g=(56*(a*a)-488*a*x+320*(x*x))/(18*(a*a)-11*a*x+x*x);
    printf("g=%f\n\n",g);
}
else if (bukva==2){
    f=-1/(sin(27*a*a+12*a*x-20*x*x-pi/2));
    printf("f=%f\n\n",f);
}
else{
    y=asin(45*a*a+46*a*x+8*x*x);
    printf("y=%f\n\n",y);
}

}