%[x,fs] = wavread('ederwander_IN_250Hz.wav');

CorrectFactor = 0.986;
threshold = 0.2;

%F0 start test
f  = 250;
fs = 44100;

signal= 0.9*sin(2*pi*f/fs*(0:9999)); 
x=signal';

framed = x(1:4096);

windowed = framed .* hann(length(framed));

FFT = fft(windowed, 4096);

FFT = FFT(1 : size(FFT,1) / 2);

FFT = abs(FFT);

% downsample by factors of 2 only
%hps1 = downsample(FFT,1);
hps2 = downsample(FFT,2);
%hps3 = downsample(FFT,3);
hps4 = downsample(FFT,4);
%hps5 = downsample(FFT,5);

y = [];

for i=1:length(hps5)

      Product =   hps1(i)  * hps2(i) * hps3(i) * hps4(i) * hps5(i);
      y(i) = [Product];
end

[m,n]=findpeaks(y, 'SORTSTR', 'descend');

Maximum = n(1);

 %try fix octave error
if (y(n(1)) * 0.5) > (y(n(2))) %& ( ( m(2) / m(1) ) > threshold )

    Maximum  = n(length(n));

end

F0 =  ( (Maximum / 4096) * fs ) * CorrectFactor 

plot(y)