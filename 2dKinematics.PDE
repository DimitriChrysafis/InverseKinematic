int numSegments = 100;
float[] x = new float[numSegments];
float[] y = new float[numSegments];
float[] angle = new float[numSegments];
float segLength = 3;
float targetX, targetY;

float ballX = 50;
float ballY = 50;
float ballXDirection = 1.0;
float ballYDirection = 1.5;
float ballXSpeed = 3.0;
float ballYSpeed = 2.0;
boolean ballIsGreen = false;

float armX = 50;
float armY = 0;
float armXAmplitude = 150.0;
float armYAmplitude = 100.0;
float armMotionFreq = 0.05;

void setup() {
  size(640, 360);
  strokeWeight(2.0);
  noFill();
  x[x.length-1] = armX;
  y[x.length-1] = armY;
}

void draw() {
  background(0);
  
  ballXSpeed += random(-0.5, 0.5);
  ballYSpeed += random(-0.5, 0.5);
  
  ballXSpeed = constrain(ballXSpeed, -4, 4); // Cap X speed to a maximum of 4
  ballYSpeed = constrain(ballYSpeed, -4, 4); // Cap Y speed to a maximum of 4
  
  ballX += ballXSpeed * ballXDirection;
  ballY += ballYSpeed * ballYDirection;
  
  if (ballX > width - 25 || ballX < 25) {
    ballXDirection *= -1; 
  }
  if (ballY > height - 25 || ballY < 25) {
    ballYDirection *= -1; 
  }
  
  ballIsGreen = checkBallCollision();
  
  if (ballIsGreen) {
    fill(0, 255, 0);
  } else {
    fill(0, 255, 255);
  }
  
  noStroke();
  ellipse(ballX, ballY, 30, 30);
  
  drawPath();
  
  armX = width / 2 + armXAmplitude * cos(armMotionFreq * frameCount);
  armY = height / 2 + armYAmplitude * sin(armMotionFreq * frameCount);
  
  x[x.length-1] = armX;
  y[x.length-1] = armY;
  
  reachSegment(0, ballX, ballY);
  for (int i = 1; i < numSegments; i++) {
    reachSegment(i, targetX, targetY);
  }
  
  for (int i = x.length - 1; i >= 1; i--) {
    positionSegment(i, i - 1);  
  }
  
  stroke(255, 100, 255);
  for (int i = 0; i < x.length; i++) {
    segment(x[i], y[i], angle[i]);
  }
}

void positionSegment(int a, int b) {
  x[b] = x[a] + cos(angle[a]) * segLength;
  y[b] = y[a] + sin(angle[a]) * segLength; 
}

void reachSegment(int i, float xin, float yin) {
  float dx = xin - x[i];
  float dy = yin - y[i];
  angle[i] = atan2(dy, dx);  
  targetX = xin - cos(angle[i]) * segLength;
  targetY = yin - sin(angle[i]) * segLength;
}

void segment(float x, float y, float a) {
  line(x, y, x + cos(a) * segLength, y + sin(a) * segLength);
}

void drawPath() {
  stroke(255, 0, 0, 150);
  noFill();
  beginShape();
  for (float angle = 0; angle < TWO_PI; angle += 0.05) {
    float px = width / 2 + armXAmplitude * cos(angle);
    float py = height / 2 + armYAmplitude * sin(angle);
    vertex(px, py);
  }
  endShape(CLOSE);
}

boolean checkBallCollision() {
  for (int i = 0; i < numSegments - 1; i++) {
    float segmentStartX = x[i];
    float segmentStartY = y[i];
    float segmentEndX = x[i+1];
    float segmentEndY = y[i+1];
    
    if (isPointNearSegment(ballX, ballY, segmentStartX, segmentStartY, segmentEndX, segmentEndY, 15)) {
      return true;
    }
  }
  return false;
}

boolean isPointNearSegment(float px, float py, float x1, float y1, float x2, float y2, float threshold) {
  float lineLength = dist(x1, y1, x2, y2);
  if (lineLength == 0) return dist(px, py, x1, y1) < threshold;
  
  float t = ((px - x1) * (x2 - x1) + (py - y1) * (y2 - y1)) / (lineLength * lineLength);
  t = constrain(t, 0, 1);
  
  float closestX = x1 + t * (x2 - x1);
  float closestY = y1 + t * (y2 - y1);
  
  return dist(px, py, closestX, closestY) < threshold;
}
