class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> prev;
        for(int i = 0; i < n ; i++){
            int d = target - nums[i];
            if(prev.find(d) != prev.end()){
                return {prev[d], i};
            }
            prev.insert({nums[i], i});
        }
        return {};
    }
};
