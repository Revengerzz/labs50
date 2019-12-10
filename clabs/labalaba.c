#define _CRT_SECURE_NO_WARNINGS

#include <locale.h>
#include <stdio.h>
#include <math.h>
int main(void)
{
	setlocale(LC_ALL, "Rus");
	float a, b, g, f, y, shag, x;
	int count, func;
	int question, i;
	float pi = 3.1415926;
	printf("Введите а: ");
	scanf("%f", &a);
	printf("Введите х: ");
	scanf("%f", &x);
	printf("Введите номер ф-ии(1/2/3): ");
	scanf("%i", &func);
	printf("Введите кол-во итераций: ");
	scanf("%i", &count);
	printf("Введите шаг: ");
	scanf("%f", &shag);
	printf("\n");
	while (count > 0)
	{
		if (count == 0)
		{
			printf("Хотите продолжить(1/2)? ");
			scanf("%i", &question);
			if (question == 1)
			{
				printf("Введите кол-во итераций: ");
				scanf("%i", &count);
				printf("Введите шаг: ");
				scanf("%f", &shag);
			}
			else
			{
				printf("Работа закончена\n");
			}
		}
		else
		{

			if (func == 1)
			{
				for (int i = 1; i <= count; i++)
				{
					if ((18 * (a*a) - 11 * a*x + x * x) == 0)
					{
						printf("Ошибка ввода данных\n");
					}
					else
					{
						g = (56 * (a*a) - 488 * a*x + 320 * (x*x)) / (18 * (a*a) - 11 * a*x + x * x);
						printf("g=%f\n\n", g);
						x = x + shag;
						a = a + shag;
						
					}
				}
			}
			if (func == 2)
			{
				for (int i = 1; i <= count; i++)
				{
					if ((sin(27 * a*a + 12 * a*x - 20 * x*x - pi / 2)) == 0)
					{
						printf("Введены неверные данные\n");
					}
					else
					{
						f = -1 / (sin(27 * a*a + 12 * a*x - 20 * x*x - pi / 2));
						printf("f=%f\n\n", f);
						x = x + shag;
						a = a + shag;
						
					}

				}
			}
			if (func == 3)
			{
				for (int i = 1; i <= count; i++)
				{
					if ((a != 0,1) && (x != 0,1))
						printf("Введены неверные данные\n");
					else
					{
						y = asin(45 * a*a + 46 * a*x + 8 * x*x);
						printf("y=%f\n\n", y);
					}
				}
			}
			
		}
		count = 0;
	}

}
