/*comment*/
#include <stdio.h>
#include <math.h>

int main(void)
{
float a,x,g,y,f;
int bukva;
double pi = 3.1415926;
printf("Введите х ");
scanf("%f", &x);
printf("Введите a ");
scanf("%f", &a);
scanf("%i",&bukva);
switch(bukva)
{
    case 1:
        g=(56*(a*a)-488*a*x+320*(x*x))/(18*(a*a)-11*a*x+x*x);
        printf("g=%f\n\n",g);
        break;
    case 2:
        f=-1/(sin(27*a*a+12*a*x-20*x*x-M_PI/2));
        printf("f=%f\n\n",f);
        break;
    case 3:
        y=asin(45*a*a+46*a*x+8*x*x);
        printf("y=%f\n\n",y);
        break;
    default:
        printf("неправильный ввод.\n");
}

}
