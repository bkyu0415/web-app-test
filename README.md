# How to install source code in AWS EC2 Server?

## A. Prerequisites

* Sign up for Amazon Web Services (AWS)
* [Use EC2 service with Windows instance (Windows_Server-2019-English-Full-Base)](http://www.dropwizard.io/1.0.2/docs/)
* Created a custom TCP inbound rule that allows TCP traffic on port 8000 anywhere
* Get the EC2 windows instance IP address

## B. Transfer source code to EC2 server
  1. Download all the source code in zip format and name as "web-app-test-master.zip"
  ![](https://i.ibb.co/C1y87Z6/image.png)
  
  2. Connect to AWS EC2 server window instance by Remote Desktop connection
  <a href="https://ibb.co/M1Csw98"><img src="https://i.ibb.co/KsrX4mN/image.png" alt="image" border="0"></a>
  
  3. Copy and Paste "web-app-test-master.zip" to "C:/"of the window instance and unzip it so that the project folder path is "C:/web-app-test-master/"
  <a href="https://ibb.co/fCxHD47"><img src="https://i.ibb.co/19mTz8x/image.png" alt="image" border="0"></a>
  	
## C. Configuration in AWS EC2 server window instance
  1. Firework setting
  * Open Windows Defender Firewall with Advanced Security through search box
  * Enter Windows Defender Firewall Properties
   <a href="https://ibb.co/34dDF68"><img src="https://i.ibb.co/XjLh50d/image.png" alt="image" border="0"></a>
  * Allow Inbound connections for Domain Profile, Private Profile and Public Profile
   <a href="https://ibb.co/RNbZ4d4"><img src="https://i.ibb.co/PMj3z0z/image.png" alt="image" border="0"></a><br />
  * Save changes and check the overview page to see whether all firewall states are on
   <a href="https://ibb.co/hVycCVn"><img src="https://i.ibb.co/ZxVSNxw/image.png" alt="image" border="0"></a>
   
   2. Time zone setting
  * Open Date & Time settings through search box
  * Set time zone to UCT(+08:00)
   <a href="https://ibb.co/mt8JTvq"><img src="https://i.ibb.co/Mp6nS8V/image.png" alt="image" border="0"></a>
    
   3. Download and install python 2.7 (https://www.python.org/downloads/) and add python.exe to Path during installation
   <a href="https://ibb.co/Q83Fj4F"><img src="https://i.ibb.co/bHMgRkg/image.png" alt="image" border="0"></a><br />
   
   4. Run the command below in the directory of "C:/web-app-test-master/"
   <a href="https://ibb.co/7zwYbYG"><img src="https://i.ibb.co/59NM2M5/image.png" alt="image" border="0"></a>
         ```
      pip install django
      ```
         ```
      pip install tzlocal
      ```      
         ```
      python ./manage.py runserver 0.0.0.0:8000
      ```      
   5. Disconnect the Remote Desktop connection while do not close the Command Prompt(keep it launching)
     <a href="https://ibb.co/2tQpmMW"><img src="https://i.ibb.co/YkMVYdP/image.png" alt="image" border="0"></a>
      
## D. Access to the web application
	 Open chrome to access urls(Assume IP is 18.219.37.17)
   * http://18.219.37.17:8000/
   * http://18.219.37.17:8000/current_time/
      
