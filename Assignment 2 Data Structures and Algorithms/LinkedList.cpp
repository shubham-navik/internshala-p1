#include <iostream>
using namespace std;

class Node {

public:
    int val;
    Node* next;

    Node(int val) {
        this->val = val;
        this->next = NULL;
    }

};

class list{
 
    private:
        int size = 0;

    public:
        Node* insert(Node* head ,int val){
            if(head == NULL){
                head = new Node(val);
                size++;
                cout << val << " Added successfully\n";
                return head;
            }
            Node *temp = head;
            while(temp->next != NULL){
                temp = temp->next;
            }
            temp->next = new Node(val);
            size++;
            cout << val << " Added successfully\n";
            return head;
        }

        Node* Delete(Node* head, int key) {
            if (head == NULL) {
                cout << "List is Empty\n";
                return head;
            }

            Node* p = NULL;
            Node* q = head;
                            
            while (q != NULL && q->val != key) {
                p = q;
                q = q->next;
            }

            // Node found to be deleted
            if (q != NULL) {
                if (p == NULL) { // If deleting the first node
                    head = q->next;
                } else {
                    p->next = q->next;
                }
                delete (q);
                size--;
                cout << "Node " << key << " deleted successfully\n";
                return head; // Return head if a node was deleted
            } else {
                cout << "Node " << key << " Not found\n";
                return head; // Return head if no node was deleted
            }
        }

        void serch(Node* head,int key){
            Node *temp = head;
            if(head == NULL){
                cout << "There is no item in LinkedList\n";
                return;
            }

            while(temp != NULL){
                if(temp->val == key){
                    cout << "Found Node " << key << endl;
                    return;
                }
                temp = temp->next;
            }

            cout << key << " Not found\n";
            return;
        }

        void traverse(Node* head){
            Node *temp = head;
            if(head == NULL){
                cout << "No, Items in list\n";
                return;
            }
            cout << "List [";
            while(temp->next != NULL){
                cout << temp->val << ",";
                temp = temp->next;
            }
            cout <<temp->val << "]"<<endl;
            return;
        }

        int getListSize(){
            return size;
        }

        int middleNode(Node* head){
            Node *slow = head;
            Node *fast = head;

            while(fast->next != NULL && fast->next->next != NULL){
                slow = slow->next;
                fast = fast->next->next;
            }

            return slow->val;
        }

        Node* mergeLists(Node* l1, Node* l2) {
            if (l1 == NULL) return l2;
            if (l2 == NULL) return l1;

            Node* mergedHead = NULL;
            if (l1->val <= l2->val) {
                mergedHead = l1;
                mergedHead->next = mergeLists(l1->next, l2);
            } else {
                mergedHead = l2;
                mergedHead->next = mergeLists(l1, l2->next);
            }
            return mergedHead;
        }

};

int main() {

    list* obj = new list();
    list* list1 = new list();
    list* list2 = new list();
    Node *head = NULL;
    Node *head2 = NULL;

    head = list1->insert(head, 2);
    // head = list1->insert(head, 3);
    // head = list1->insert(head, 4);
    // head = list1->insert(head, 5);
    // head = list1->insert(head, 6);
    // head = list1->insert(head, 7);
    // head = list1->insert(head, 8);
    // int x = list1->getListSize();
    // cout << x;
    // head = list1->Delete(head,5);
    // head = list1->Delete(head,2);
    // head = list1->Delete(head,4);
    // x = list1->getListSize();
    // cout << x;
    // list1->serch(head,5);
    head2 = list2->insert(head2, 2+1);
    head2 = list2->insert(head2, 3+1);
    head2 = list2->insert(head2, 4+1);
    // head2 = list2->insert(head2, 5+1);
    // head2 = list2->insert(head2, 6+1);
    // head2 = list2->insert(head2, 7+1);
    // head2 = list2->insert(head2, 8+1);
    list1->traverse(head);
    cout << list1->middleNode(head) << endl;
    list2->traverse(head2);
    Node* mergedlist = obj->mergeLists(head, head2);
    obj->traverse(mergedlist);

    return 0; 
}
