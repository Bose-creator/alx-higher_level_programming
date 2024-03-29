#!/usr/bin/python3
#include <stdlib.h>
typedef struct listint_s {
    int number;
    struct listint_s *next;
} listint_t;
listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node, *current;
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return NULL;
    new_node->number = number;
    if (*head == NULL || (*head)->number >= number) {
        new_node->next = *head;
        *head = new_node;
    } else {
        current = *head;
        while (current->next != NULL && current->next->number < number) {
            current = current->next;
        }
        new_node->next = current->next;
        current->next = new_node;
    }

    return new_node;
}
