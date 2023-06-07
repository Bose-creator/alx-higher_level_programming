#include "lists.h"

/**
 * check_cycle - it checks if a singly linked list has
 * a cycle in it.
 * @list: pointer to the list
 * Return: return 0 if there is no cycle,
 * and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *prc2;
	listint_t *provi;

	prc2 = list;
	provi = list;
	while (list && prc2 && prc2->next)
	{
		list = list->next;
		prc2 = prc2->next->next;

		if (list == prc2)
		{
			list = provi;
			provi =  prc2;
			while (1)
			{
				prc2 = provi;
				while (prc2->next != list && prc2->next != provi)
				{
					prc2 = prc2->next;
				}
				if (prc2->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
