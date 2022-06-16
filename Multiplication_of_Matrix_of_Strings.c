/*
Write a C program for the task as described below.
(a) Define and allocate space for two n × n matrices M1 and M2 of strings, where n is read as
input. The entries of M1 must be read in row major order as strings of length at most 19. Print
M1 in a suitable manner row-wise. The entries of M2 must be strings of length at most 38.
[20 Marks]
(b) Compute the square of M1 in M2. Print M2 in a suitable manner row-wise. [20 Marks]
Sample Output: If M1 is the 2 × 2 matrix

  Somnath   Hazra
 [               ]
  Gunjan    Balde 

then M2 = M1 × M1 is

  SomnathSomnath  SomnathHazra
 [                             ]
  GunjanSomnath   GunjanHazra 

Note: The modified multiplication and addition operations for string elements of the matri-
ces are respectively concatenation (||) and lexicographic maximization (max). For example

multiplication of the strings Gunjan and Hazra results in the product string GunjanHazra,
which is lexicographically smaller than the product string BaldeBalde, making GunjanHazra
to be the entry of M2[1][1]. So we obtain the entry M2[1][1] by evaluating the expression:

max(M1[1][0]||M1[0][1], M1[1][1]||M1[1][1])·
*/



#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *max(char a[], char b[])
{
    if ((strcmp(a, b)) > 0)
        return a;
    else
        return b;
}

int main()
{
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);

    char ***M1 = (char ***)malloc(n * sizeof(char **));
    char ***M2 = (char ***)malloc(n * sizeof(char **));

    printf("Enter the matrix M1:\n");
    for (int i = 0; i < n; i++)
    {
        M1[i] = (char **)malloc(n * sizeof(char *));
        for (int j = 0; j < n; j++)
        {
            M1[i][j] = (char *)malloc(19 * sizeof(char));
            scanf("%s", M1[i][j]);
        }
    }

    printf("\nMatrix M1:\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            printf("%s     ", M1[i][j]);
        printf("\n");
    }

    for (int i = 0; i < n; ++i)
    {
        M2[i] = (char **)malloc(n * sizeof(char *));
        for (int j = 0; j < n; ++j)
        {
            M2[i][j] = (char *)malloc(38 * sizeof(char));

            char *res = (char *)malloc(38 * sizeof(char));

            strcpy(res, M1[i][0]);
            strcat(res, M1[0][j]);
            for (int k = 0; k < n; ++k)
            {
                char *temp = (char *)malloc(38 * sizeof(char));
                strcpy(temp, M1[i][k]);
                strcat(temp, M1[k][j]);
                strcpy(res, max(res, temp));
            }
            strcpy(M2[i][j], res);
        }
    }

    printf("\nMatrix M2:\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            printf("%s     ", M2[i][j]);
        printf("\n");
    }
}
