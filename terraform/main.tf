resource "aws_instance" "ec2" {

  ami= "ami-0224820b4e90b6949"
  instance_type = "t2.micro"
  
  count =2
  subnet_id = element([ "subnet-09c70bcefed00afad", "subnet-08a89211d52d8b7f7"], count.index)          # in netwrok setting edit select vpc custome with this id
  availability_zone      = element(["us-east-1a", "us-east-1b"], count.index)


  vpc_security_group_ids = ["sg-065d6e671aceef7be"]   # netwrok setting security group id virtul private culture

  

  #iam_instance_profile = "ssm-role"  
 
  tags = {
    Name = "shreet_admission_app-${count.index}"
  }

}
 