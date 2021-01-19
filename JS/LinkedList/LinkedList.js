import LinkedListNode from './LinkedListNode';

export default class LinkedList {
	constructor(){
		// head and tail are nodes
		this.head = null;
		this.tail = null;
	}


	prepend(value){
		// make a new node as head
		const newNode = new LinkedListNode(value, this.head);

		this.head = newNode;

		if(!this.tail){
			this.tail = newNode;
		}

		return this;
	}

	append(value){
		const newNode = new LinkedListNode(value);

		if(!this.head){
			this.head = newNode;
			this.tail = newNode;
			return this;
		}

		const currentTail = this.tail;
		currentTail.next = newNode;
		this.tail = newNode;

		return this;

	}

	delete(){

	}

	deleteHead(){

	}

	deleteTail(){
	
	}

	toString(){

	}

	toArray(){

	}
}
