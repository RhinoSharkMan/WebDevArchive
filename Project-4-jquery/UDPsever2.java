import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class ServerUDP {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java ServerUDP <port>");
            return;
        }
        
        int port = Integer.parseInt(args[0]);

        try {
            DatagramSocket socket = new DatagramSocket(port);
            byte[] buffer = new byte[1024];
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
            
            System.out.println("Server is running and waiting for client message...");

            // Receive data from the client
            socket.receive(packet);
            String message = new String(packet.getData(), 0, packet.getLength());
            System.out.println("Received from client: " + message);

            // Convert message to uppercase
            String modifiedMessage = message.toUpperCase();
            String serverName = InetAddress.getLocalHost().getHostName();
            String response = modifiedMessage + " (From server: " + serverName + ")";

            // Send modified message back to client
            InetAddress clientAddress = packet.getAddress();
            int clientPort = packet.getPort();
            byte[] responseData = response.getBytes();
            DatagramPacket responsePacket = new DatagramPacket(responseData, responseData.length, clientAddress, clientPort);
            socket.send(responsePacket);
            
            socket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}