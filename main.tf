resource "local_file" "file1"{
  filename= "my_first_file"
  content= "This is my first terraform file"
}

resource "random_pet" "pet"{
}


