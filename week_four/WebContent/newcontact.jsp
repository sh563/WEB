<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<%@ page import="java.io.*"%>
<%@ page import="java.io.FileWriter"%>
<%@ page import="java.util.Scanner"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">

</head>
<body>
	<%
		
	String username = request.getParameter("un");

	String password = request.getParameter("secure");
	

	File myObj = new File("C:\\Users\\anjal\\Desktop\\java\\week_four\\MyDB.txt");
	FileOutputStream fw = new FileOutputStream(myObj);

	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fw));

	bw.write("anjali,1234");
	bw.newLine();
	bw.write("Preeti,5678");
	bw.newLine();
	bw.write("Vicky,9123");
	bw.newLine();
	bw.write("Raiz,1238");
	bw.newLine();
	bw.close();

	if (myObj.createNewFile()) 
	{
		out.write("File created: " + myObj.getName());

	} 
	else
	{
	if (request.getParameter("b1") != null) 
	{
			
			
			BufferedReader reader1 = new BufferedReader(new FileReader(myObj));	
			String line1 = reader1.readLine();
			
			while(line1!=null)
			{
				if(line1.equalsIgnoreCase(username+","+password))
				{
					out.write("Welcome to our website!! You are logged in successfully!!");
					break;
					
				}
				else
				{
					out.write("-------Please check Your username and password again!!-----------");
				}
				
				line1 = reader1.readLine();
			}reader1.close();
		} 
	else 
	{
			if (request.getParameter("b2") != null)
			{
				FileWriter fw1 = null; 
				BufferedWriter bw1 = null;
				PrintWriter pw = null; 
			 
				fw1 = new FileWriter("C:\\Users\\anjal\\Desktop\\java\\week_four\\MyDB.txt", true); 
				bw1 = new BufferedWriter(fw1); 
				pw = new PrintWriter(bw1); 
				pw.println(username+","+password); 
				
				out.print("THANK YOU FOR REGISTERATION!! YOU ARE SUCCESSFULLY REGISTERED!!");
			    pw.close();
			    bw1.close();
				fw1.close();
				   
				
				
				

				
			}
		
			
		
	}
	}
	%>
</body>
</html>