#include<iostream>
using namespace std;
 int main()
 {
    /*c++ program for addition,subtraction,multiplication and disision using switch*/
    float a, b,rem;
    int ch, q;

    cout <<"Arithmetic operations";
    cout <<"\n1.Addition\n2.subraction\n3.Multiplication";
    cout <<"\n\nEnter your choice:\n";
    cin >> ch;

    switch (ch)
    {
        case 1:
        {
            cout<<"Enter two nums:";
            cin>>a>>b;
            rem = a+b;
            cout<<rem;
        }
        break;
        
        case 2:
        {
            cout<<"Enter two nums:";
            cin>>a>>b;
            rem = a-b;
            cout<<rem;
        }
        break;
        
        case 3:
        {
            cout<<"Enter two nums:";
            cin>>a>>b;
            rem = a+b;
            cout<<rem; 
        }
        break;

        case 4:
        {
             cout<<"Enter two nums:";
            cin>>a>>b;
            rem = a+b;
            cout<<rem;
        }
        break;
    }
    return 0;
}