# How to install source code in AWS EC2 Server（Ubuntu Instance）?

## A. Prerequisites

* Sign up for Amazon Web Services (AWS)
* Use EC2 service with Ubuntu instance
* Get key file in .pem format
* Get the EC2 windows instance IP address
* Install Putty and FileZilla

## B. Connect local machine to Ubuntu instance by Putty
  1. Convert key file in .pem format to .ppk format by PuTTYgen. Load the .pem file and save private key to .ppk file
  <a href="https://ibb.co/HqvSmCJ"><img src="https://i.ibb.co/4pyqB2Q/image.png" alt="image" border="0"></a>
  
  2. Transfer source code to EC2 server ubuntu instance by FileZilla and .ppk key file
  <a href="https://ibb.co/zQQTQR3"><img src="https://i.ibb.co/177t7qC/image.png" alt="image" border="0"></a><br />
  Drag the project folder in local machine to Ubuntu instance under the path /home/ubuntu/web-app-test-master
  <a href="https://ibb.co/QpLFpQH"><img src="https://i.ibb.co/mbkCbTy/image.png" alt="image" border="0"></a>
  
  3. Connect to AWS EC2 server ubuntu instance by Putty using .ppk key file
  <a href="https://ibb.co/CPCGddM"><img src="https://i.ibb.co/qJqQGGW/image.png" alt="image" border="0"></a>
  After connection:
  <a href="https://ibb.co/nrQtfRL"><img src="https://i.ibb.co/Y2fw8bL/image.png" alt="image" border="0"></a>
  	
## C. Configuration in AWS EC2 server ubuntu instance  
  1. Install python2 and required packages
      ```
      sudo apt update
      ```
      ```
      sudo apt install python2
      ```      
      ```
      curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py
      ```    
      ```
      sudo python2 get-pip.py
      ```
      ```
      pip2 install django
      ```      
      ```
      pip2 install tzlocal
      ```   
      ```
      python2 manage.py migrate
      ```
      ```
      nohup python2 ./manage.py runserver 0.0.0.0:8000
      ```      

   2. Time zone setting
      ```
      pip2 install tzlocal
      ```   

## D. Access to the web application
	 Open chrome to access urls(Assume IP is 18.219.37.17)
   * http://18.219.37.17:8000/
   * http://18.219.37.17:8000/current_time/
      
