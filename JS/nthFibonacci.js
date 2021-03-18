function getNthFib(n) {
  // Write your code here.
	
	let prev = 0;
	let next = 1;
	let fib = 0;	
	
	for(i=prev; i<n-1; i++){
		fib = prev + next;
		prev = next;
		next = fib;
	}
	
	return prev;
}

console.log(getNthFib(2))//0,1,1
console.log(getNthFib(6))//0,1,1,2,3,5