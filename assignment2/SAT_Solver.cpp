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
{ int n,nc;
  cin>>n>>nc;
  vector<vector<int>>v;
  for(int i=0;i<nc;i++){
      vector<int>v1;
      int c=1;
      while(c){
          cin>>c;
          if(c)
          v1.push_back(c);
      }
      v.push_back(v1);
  }
  std::sort(v.begin(),v.end(),[](const vector<int>&a, const vector<int>&b){return a.size()<b.size();})
  
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
