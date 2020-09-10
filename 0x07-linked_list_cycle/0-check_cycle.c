#include"lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: singly linked list
 * Return: 1 if there is no cycle or 0 if it is not.
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *prev;

	if (list == NULL || list->next == NULL)
		return (0);

	head = prev = list;

	while (head && prev && prev->next != NULL)
	{
		head = head->next;
		prev = prev->next->next;
		if (head == prev)
			return (1);
	}
	return (0);
}
