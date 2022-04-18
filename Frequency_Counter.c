// Frequency counter

#include <stdio.h>
#include <string.h>
#define n 150

void maxchar(char str[n])
{
    int count[n] = {0}, max = 0;
    char result;
    for (int i = 0; i < strlen(str); i++)
    {
        count[str[i]]++;
        if (max < count[str[i]])
        {
            max = count[str[i]];
            result = str[i];
        }
    }
    printf("%c with number of occurance %d\n", result, max);
    for (int i = 0; i < strlen(str); i++)
    {
        for (int k = 0; k < max; k++)
        {
            if (str[i] == result)
            {
                memmove(&str[i], &str[i + 1], strlen(str) - i);
            }
        }
    }
}

int main()
{
    char str[n];

    printf("Enter the string: ");
    scanf("%s", str);
    printf("Maximum occuring character is:\n");
    for (int j = 0; j < strlen(str); j++)
    {
        maxchar(str);
    }
}
