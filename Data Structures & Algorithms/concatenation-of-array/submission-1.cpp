class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> res;
        int i = 0;
        for(; i < nums.size(); i++){
            res.push_back(nums[i]);
        }
        for(int j = 0; j < nums.size(); j++){
            res.push_back(nums[j]);
        }
        return res;
    }
};