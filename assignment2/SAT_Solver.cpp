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

vector dpll(vector<int>v,vector<int>val,vector<pair<int,int>>sign){
    




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
  for(int i=0;i<nc;i++){
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
  for(int i=0;i<n && v.size()<=1;i++){
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
  for(int i=0;i<n && f==0;i++){
      if(sign[i].first==1 && sign[i].second==0)
          val[i]=1;
      if(sign[i].first==0 && sign[i].second==1)
          val[i]=0;
  }
  for(int i=0;i<nc;i++){
      for(int j=0;j<v[i].size();j++){
          int t=v[i][j];
          if(t>0 && val[i][j]==1){
              v.erase(v.begin()+i);
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
