//create a class person
//Member variables- first_name,last_name and address
//Member functions- getFullName(), getAddress()

//create an object Tom Cruise and print out his information on your webpage

class Person {
	constructor(first_name,last_name,address){
		this.first_name= first_name;
		this.last_name=last_name;
		this.address=address;
	}
	getFullName(){
		document.getElementById("myName").innerHTML = this.first_name + " " + this.last_name;
		//or you can have -------return this.first_name + "" + this.last_name:	
	}
	getAddress(){
		document.getElementById("myAddress").innerHTML = this.address;
		//or you can put----- return this.address;

	}

}

var MC = new person("Tom","Cruise","NY");
MC.getFullName();
MC.getAddress();

