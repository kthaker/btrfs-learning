#include <stdlib.h>
#include "btree.h"

btree_t *create_btree()
{
    btree_t *root = (btree_t *)malloc(sizeof(btree_t));
    root->is_leaf = 1;
    root->key_num = 0;

    return root;
}
