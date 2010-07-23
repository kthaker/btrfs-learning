#ifndef _BTREE_H
#define _BTREE_H

/* Create, Insert, Delete, Search */

#define k   2

typedef int     key_t;
typedef char *  value_t;

typedef struct _btree_t
{
    int             is_leaf;
    int             key_num;
    key_t           key[2 * k - 1];
    value_t         value;
    struct _btree_t *child[2 * k];
} btree_t;


btree_t *create_btree();
void insert_node(btree_t *root, key_t key, value_t value);
void delete_node(btree_t *root, key_t key);
void search_key(btree_t *root, key_t key);

#endif
