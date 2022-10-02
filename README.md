VYASA - DEVICE FOR EFFIECIENT STUDY AT RURALS

Abstract :
The deterioration of India's educational system has been a major source of concern for several decades, yet no significant improvement in rural areas has been observed. The primary issues in rural areas include, absence of appropriate schools and access to excellent education, lack of bandwidth and other connectivity issues. Thanks to technological improvements, access to high- quality education is no longer a luxury for people living in rural areas, thanks to the rise of learning apps. Our simple yet efficient solution comes with powerful features and contains all necessary educational content:

● No internet requirement: to access the educational content.

● Quality education: will build a connection between students and teachers.

● Under one roof: all the educational content can be accessed.

● Open Access Content: can be accessed by and added upon by users.

● Community for learners: where notes can be shared and allows peer-to-peer and mentor to mentorship and guidance.

Methodology :
 
Education is rapidly gravitating towards more virtual ,distributive sector that involves cutting-edge technology.With advanced and upgraded technologies, this mode of learning has been made simpler. Major innovations are altering and will continue to impact the education sector. This fusion of modern technology and education can help in a variety of ways, solving the much required need for creating educated citizens.
Our product will create a bridge among online and off-line median which will transmit the fetched data to multiple users through Wi-Fi direct at a time.
The product will allow mobile phones to connect with bridge adapter without internet connection through Wifi within a radius of 100 metres.

<img width="485" alt="image" src="https://user-images.githubusercontent.com/67583008/190897414-63a14d7b-1426-45c3-8b35-78b7895a7837.png">

● Mentors will send data to Organisations.

● They will further filter and classify the data that is it reliable or not for posting.

● After classification, Data will be uploaded to panel though Internet.

ADMIN PANEL

In admin panel we will allow authorised personnel to upload the data ( notes , videos and other thing ) to FCM cloud server which will get Stored in Google Cloud Storage which is accessible by the bridge adapter.
Data will be stored in online cloud which will be accessible through Bridge Adapter.

BRIDGE ADAPTER

We will create a brigade adapter which is device designed in raspberry pi which will hold the content on a virtual cloud firebase server and download it offline whenever gets minimum ping.

Bridge adapter is a device which is holding a wifi module and a custom script that is giving a ping at every second to the database and whenever the ping hit back . It will download the content offline and provide it to the device which is connecting through our app via Wifi Direct. Bridge adapter act as a local host for the mobile app.

MOBILE APP

In mobile app we will create a feature that it will connect to the bridge via wifi Direct and allow user to fetch the downloaded content from the bridge , multiple users at a same time can access the content which is available offline by a bridge adapter. Then the mobile phone through wifi Direct feature on our app which is developed in Android studio can connect to the device bridge adapter and allow content to be available offline to the user.

Now as a part of admin NGO or any organisation can maintain the data on bridge adapter through admin panel.

There will be 2 way communication which will allow user to send student’s feedback and query to mentors as well.

Students can post their feedback or queries through mobile app locally without internet connection which will get stored in Bridge Adapter. Whenever Bridge Adapter will get minimum ping, It will send that data to admin panel which can further be shared with teachers and mentors.

Technologies using:-

● Firebase Cloud Storage

● FCM server

● CRUD functionalities on Bridge Adapter ( Custom script working on Pi)

● Admin Panel (Website)

● Mobile App ( Android studio, SQLite , Firebase)

● Internet of Things
 
