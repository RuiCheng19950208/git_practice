class Solution {
public:
    int searchInsert(vector<int>& nums, int target) 
    {
        int ans=0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i]<target)
            {
                ans++;
            }
            else{return ans;}
        }
        return ans;
    }
};