/*
noise.h and noise.c are needed for this Game
*/

#ifndef _noise_h_
#define _noise_h_

void seed(unsigned int x);

float simplex2(
    float x, float y,
    int octaves, float persistence, float lacunarity);

float simplex3(
    float x, float y, float z,
    int octaves, float persistence, float lacunarity);

#endif
