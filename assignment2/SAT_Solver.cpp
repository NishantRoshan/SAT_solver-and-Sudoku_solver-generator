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
  for(int i=0;i<nc && v[i].size()<=1;i++){
      if(v[i].size()==0)
      v.erase(v.begin()+i);
      if(v[i].size()==1){
          int t=v[i][0];
          if(t>0 && v[t-1]!=0)
          v[t-1]=1;
          else if(t<0 && v[t-1]!=1)
          v[t-1]=0;
          else
          f=1;
          v.erase(v.begin()+i);
      }
  }
  for()
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
