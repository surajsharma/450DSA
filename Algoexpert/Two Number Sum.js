function twoNumberSum(array, targetSum) {
	let nums = []
	array.forEach((x, i) => {
		array.reduce((a,b,i2)=>{
			if(x+b == targetSum){
				if(i !== i2 && x!= targetSum){
					nums.push(x)
					if(array.length == 2 || array.length== 3 || x == 0){
						nums.push(b)
					}
				}
			}
		})
	})
	
	return nums
}

//let pa = twoNumberSum([1,2,3,4,5,9,0], 9)
//pa = twoNumberSum([3,5,-4,8,11,1,-1,6], 10)
let pa = twoNumberSum([4, 6, 1], 5)
console.log(pa)