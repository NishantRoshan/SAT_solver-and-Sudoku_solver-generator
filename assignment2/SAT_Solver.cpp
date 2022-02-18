#include "dimacs_to_vector.h"           //include the local file to get the cnf formula in vector of vector form
#include<bits/stdc++.h>
using namespace std;
 
#define int long long
#define rep(i,a,b) for(int i=a; i<b; ++i)
#define all(x) x.begin(),x.end()
#define mp make_pair
#define google "Case #" << tc << ": "
 
const long long INF=1e18;
const int32_t M=1e9+7;
const int32_t MM=998244353;
const int32_t N=1e5+1;

vector dpll(vector<int>v,vector<int>val,vector<pair<int,int>>sign){           //vector pair sign stores the number
       for(int i=0;i<sign.size();i++){                                        //of times a literal comes in positive and negative form
           sign[i].first=0;                      //sign.first means it comes in p form
           sign[i].second=0;                     //sign.second means it comes in ~p form
       }       
       for(int i=0;i<v.size();i++){
           for(int j=0;j<v[i].size();j++){
               int k=v[i][j];
               if(v[i][j]>0)                     
               sign[k-1].first++;                //increase count of positive for a particular literal
               else
               sign[-k-1].second++;              //increase count of negative for a particular literal
           }
       }
       
}
void solve(int tc)
{ int n,nc,f=0;
  cin>>n>>nc;
  vector<int>val;
  vector<pair<int,int>>sign;
  for(int i=0;i<n;i++)
      sign.push_back(make_pair(0,0));
  for(int i=0;i<n;i++)
  val.push_back(-1);
  vector<vector<int>>v;
  for(int i=0;i<nc;i++){                          //checking for unit clauses
      vector<int>v1;
      int c=1;
      while(c){
          cin>>c;
          if(c){
          v1.push_back(c);
          int k=abs(c);
          if(c>0)
          sign[k-1].first++;
          else
          sign[k-1].second++;
          }
      }
      v.push_back(v1);
  }
  std::sort(v.begin(),v.end(),[](const vector<int>&a, const vector<int>&b){return a.size()<b.size();})
  for(int i=0;i<n && v.size()<=1;i++){                //checking for pure literals, which appear in same sign
      int t=v[i][0];
      if(t>0 && val[t-1]!=0)
      val[t-1]==1;
      else if(t<0 && val[-t-1]!=1)
      val[-t-1]==0;
      else
      f=1;
  }
  for
  if(f==1)
  cout<<"Unsatisfiable"<<endl;
  else{
  for(int i=0;i<n && f==0;i++){                     //assigning values to pure literals
      if(sign[i].second==0)
          val[i]=1;
      else if(sign[i].first==0)
          val[i]=0;
  }
  for(int i=0;i<v.size();i++){
      for(int j=0;j<v[i].size();j++){
          int t=v[i][j];
          if((t>0 && val[t-1]==1) || (t<0 && val[-t-1]==0)){
              v.erase(v.begin()+i);                 //deleting clauses which have been assigned values
              i--;
              break;
          }
      }
  }
    dpll(v,val,sign);
 }
}
int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    solve(t);
}
