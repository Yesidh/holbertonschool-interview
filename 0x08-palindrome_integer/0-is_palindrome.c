#include "palindrome.h"

/**
 * is_palindrome - check if a number is palindrome
 * @n: value to check
 * Return: 1 if it's palindrome 0 if not
 */

int is_palindrome(unsigned long n)
{

	int n_copy = 0, mod_n = 0, sum = 0;

	for (n_copy = n; n != 0; n /= 10)
	{
		mod_n = n % 10;
		sum = sum * 10 + mod_n;
	}

	if (n_copy == sum)
		return (1);
	else
		return (0);

	return (EXIT_SUCCESS);
}
