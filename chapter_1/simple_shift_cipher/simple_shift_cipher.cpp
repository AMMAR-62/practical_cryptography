#include <bits/stdc++.h>

using namespace std;

void simpleShiftCipher(string &str, int shift){
    for(int i=0; i<str.size(); i++){
        if(isupper(str[i]))
        str[i] = char((str[i]+shift-65)%26+65);
        else
        str[i] = char((str[i]+shift-97)%26+97);
    }
    return;
}

int main(){
    // cout << int('z');
    string str; cin>>str;
    int shift; cin>>shift;
    simpleShiftCipher(str, shift);
    cout << str;
    
    return 0;
}