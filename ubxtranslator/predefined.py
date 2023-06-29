"""Predefined message classes"""

from . import core

__all__ = ['ACK_CLS', 'NAV_CLS', ]

ACK_CLS = core.Cls(0x05, 'ACK', [
    core.Message(0x01, 'ACK', [
        core.Field('clsID', 'U1'),
        core.Field('msgID', 'U1'),
    ]),
    core.Message(0x01, 'NAK', [
        core.Field('clsID', 'U1'),
        core.Field('msgID', 'U1'),
    ])
])

NAV_CLS = core.Cls(0x01, 'NAV', [
    core.Message(0x60, 'AOPSTATUS', [
        core.Field('iTOW', 'U4'),
        core.Field('aopCfg', 'U1'),
        core.Field('status', 'U1'),
        core.PadByte(repeat=9),
    ]),
    core.Message(0x05, 'ATT', [
        core.Field('iTOW', 'U4'),
        core.Field('version', 'U1'),
        core.PadByte(repeat=2),
        core.Field('roll', 'I4'),
        core.Field('pitch', 'I4'),
        core.Field('heading', 'I4'),
        core.Field('accRoll', 'U4'),
        core.Field('accPitch', 'U4'),
        core.Field('accHeading', 'U4'),
    ]),
    core.Message(0x22, 'CLOCK', [
        core.Field('iTOW', 'U4'),
        core.Field('clkB', 'I4'),
        core.Field('clkD', 'I4'),
        core.Field('tAcc', 'U4'),
        core.Field('fAcc', 'U4'),
    ]),
    core.Message(0x31, 'DGPS', [
        core.Field('iTOW', 'U4'),
        core.Field('age', 'I4'),
        core.Field('baseId', 'I2'),
        core.Field('baseHealth', 'I2'),
        core.Field('numCh', 'U1'),
        core.Field('status', 'U1'),
        core.PadByte(repeat=1),
        core.RepeatedBlock('RB', [
            core.Field('svid', 'U1'),
            core.BitField('flags', 'X1', [
                core.Flag('channel', 0, 4),
                core.Flag('dgpsUsed', 4, 5),
            ]),
            core.Field('ageC', 'U2'),
            core.Field('prc', 'R4'),
            core.Field('prrc', 'R4'),
        ])
    ]),
    core.Message(0x04, 'DOP', [
        core.Field('iTOW', 'U4'),
        core.Field('gDOP', 'U2'),
        core.Field('pDOP', 'U2'),
        core.Field('tDOP', 'U2'),
        core.Field('vDOP', 'U2'),
        core.Field('hDOP', 'U2'),
        core.Field('nDOP', 'U2'),
        core.Field('eDOP', 'U2'),
    ]),
    core.Message(0x61, 'EOE', [
        core.Field('iTOW', 'U4'),
    ]),
    core.Message(0x39, 'GEOFENCE', [
        core.Field('iTOW', 'U4'),
        core.Field('version', 'U1'),
        core.Field('status', 'U1'),
        core.Field('numFences', 'U1'),
        core.Field('combState', 'U1'),
        core.RepeatedBlock('RB', [
            core.Field('state', 'U1'),
            core.PadByte(),
        ]),
    ]),
    core.Message(0x13, 'HPPOSECEF', [
        core.Field('version', 'U1'),
        core.PadByte(repeat=2),
        core.Field('iTOW', 'U4'),
        core.Field('ecefX', 'I4'),
        core.Field('ecefY', 'I4'),
        core.Field('ecefZ', 'I4'),
        core.Field('ecefXHp', 'I1'),
        core.Field('ecefYHp', 'I1'),
        core.Field('ecefZHp', 'I1'),
        core.PadByte(),
        core.Field('pAcc', 'U4'),
    ]),
    core.Message(0x14, 'HPPOSLLH', [
        core.Field('version', 'U1'),
        core.PadByte(repeat=2),
        core.Field('iTOW', 'U4'),
        core.Field('lon', 'I4'),
        core.Field('lat', 'I4'),
        core.Field('height', 'I4'),
        core.Field('hMSL', 'I4'),
        core.Field('lonHp', 'I1'),
        core.Field('latHp', 'I1'),
        core.Field('heightHp', 'I1'),
        core.Field('hMSLHp', 'I1'),
        core.Field('hAcc', 'U4'),
        core.Field('vAcc', 'U4'),
    ]),
    core.Message(0x09, 'ODO', [
        core.Field('version', 'U1'),
        core.PadByte(repeat=2),
        core.Field('iTOW', 'U4'),
        core.Field('distance', 'U4'),
        core.Field('totalDistance', 'U4'),
        core.Field('distanceStd', 'U4'),
    ]),
    core.Message(0x34, 'ORB', [
        core.Field('iTOW', 'U4'),
        core.Field('version', 'U1'),
        core.Field('numSv', 'U1'),
        core.PadByte(repeat=1),
        core.RepeatedBlock('RB', [
            core.Field('gnssId', 'U1'),
            core.Field('svId', 'U1'),
            core.BitField('svFlag', 'X1', [
                core.Flag('health', 0, 2),
                core.Flag('visibility', 2, 4),
            ]),
            core.BitField('eph', 'X1', [
                core.Flag('ephUsability', 0, 5),
                core.Flag('ephSource', 5, 8),
            ]),
            core.BitField('alm', 'X1', [
                core.Flag('almUsability', 0, 5),
                core.Flag('almSource', 5, 8),
            ]),
            core.BitField('otherOrb', 'X1', [
                core.Flag('anoAopUsability', 0, 5),
                core.Flag('type', 5, 8),
            ]),
        ]),
    ]),
    core.Message(0x01, 'POSECEF', [
        core.Field('iTOW', 'U4'),
        core.Field('ecefX', 'I4'),
        core.Field('ecefY', 'I4'),
        core.Field('ecefZ', 'I4'),
        core.Field('pAcc', 'U4'),
    ]),
    core.Message(0x02, 'POSLLH', [
        core.Field('iTOW', 'U4'),
        core.Field('lon', 'I4'),
        core.Field('lat', 'I4'),
        core.Field('height', 'I4'),
        core.Field('hMSL', 'I4'),
        core.Field('hAcc', 'U4'),
        core.Field('vAcc', 'U4'),
    ]),
    core.Message(0x07, 'PVT', [
        core.Field('iTOW', 'U4'),
        core.Field('year', 'U2'),
        core.Field('month', 'U1'),
        core.Field('day', 'U1'),
        core.Field('hour', 'U1'),
        core.Field('min', 'U1'),
        core.Field('sec', 'U1'),
        core.BitField('valid', 'X1', [
            core.Flag('validDate', 0, 1),
            core.Flag('validTime', 1, 2),
            core.Flag('fullyResolved', 2, 3),
            core.Flag('validMag', 3, 4),
        ]),
        core.Field('tAcc', 'U4'),
        core.Field('nano', 'I4'),
        core.Field('fixType', 'U1'),
        core.BitField('flags', 'X1', [
            core.Flag('gnssFixOK', 0, 1),
            core.Flag('diffSoln', 1, 2),
            core.Flag('psmState', 2, 5),
            core.Flag('headVehValid', 5, 6),
            core.Flag('carrSoln', 6, 8),
        ]),
        core.BitField('flags2', 'X1', [
            core.Flag('confirmedAvai', 5, 6),
            core.Flag('confirmedDate', 6, 7),
            core.Flag('confirmedTime', 7, 8),
        ]),
        core.Field('numSV', 'U1'),
        core.Field('lon', 'I4'),
        core.Field('lat', 'I4'),
        core.Field('height', 'I4'),
        core.Field('hMSL', 'I4'),
        core.Field('hAcc', 'U4'),
        core.Field('vAcc', 'U4'),
        core.Field('velN', 'I4'),
        core.Field('velE', 'I4'),
        core.Field('velD', 'I4'),
        core.Field('gSpeed', 'I4'),
        core.Field('headMot', 'I4'),
        core.Field('sAcc', 'U4'),
        core.Field('headAcc', 'U4'),
        core.Field('pDOP', 'U2'),
        core.PadByte(5),
        core.Field('headVeh', 'I4'),
        core.Field('magDec', 'I2'),
        core.Field('magAcc', 'U2'),
    ]),
    core.Message(0x3C, 'RELPOSNED', [
        core.Field('version', 'U1'),
        core.PadByte(),
        core.Field('refStationId', 'U2'),
        core.Field('iTOW', 'U4'),
        core.Field('relPosN', 'I4'),
        core.Field('relPosE', 'I4'),
        core.Field('relPosD', 'I4'),
        core.Field('relPosLength', 'I4'),
        core.Field('relPosHeading', 'I4'),
        core.PadByte(repeat=3),
        core.Field('relPosHPN', 'I1'),
        core.Field('relPosHPE', 'I1'),
        core.Field('relPosHPD', 'I1'),
        core.Field('relPosHPLength', 'I1'),
        core.Field('accN', 'U4'),
        core.Field('accE', 'U4'),
        core.Field('accD', 'U4'),
        core.Field('accLength', 'U4'),
        core.Field('accHeading', 'U4'),
        core.PadByte(repeat=3),
        core.BitField('flags', 'X4', [
            core.Flag('gnssFixOK', 0, 1),
            core.Flag('diffSoln', 1, 2),
            core.Flag('relPosValid', 2, 3),
            core.Flag('carrSoln', 3, 5),
            core.Flag('isMoving', 5, 6),
            core.Flag('refPosMiss', 6, 7),
            core.Flag('refObsMiss', 7, 8),
        ]),
    ]),
    core.Message(0x35, 'SAT', [
        core.Field('iTOW', 'U4'),
        core.Field('version', 'U1'),
        core.Field('numSvs', 'U1'),
        core.PadByte(repeat=1),
        core.RepeatedBlock('RB', [
            core.Field('gnssId', 'U1'),
            core.Field('svId', 'U1'),
            core.Field('cno', 'U1'),
            core.Field('elev', 'I1'),
            core.Field('azim', 'I2'),
            core.Field('prRes', 'I2'),
            core.BitField('flags', 'X4', [
                core.Flag('qualityInd', 0, 3),
                core.Flag('svUsed', 3, 4),
                core.Flag('health', 4, 6),
                core.Flag('diffCorr', 6, 7),
                core.Flag('smoothed', 7, 8),
                core.Flag('orbitSource', 8, 11),
                core.Flag('ephAvail', 11, 12),
                core.Flag('almAvail', 12, 13),
                core.Flag('anoAvail', 13, 14),
                core.Flag('aopAvail', 14, 15),
                core.Flag('sbasCorrUsed', 16, 17),
                core.Flag('rtcmCorrUsed', 17, 18),
                core.Flag('slasCorrUsed', 18, 19),
                core.Flag('prCorrUsed', 20, 21),
                core.Flag('crCorrUsed', 21, 22),
                core.Flag('doCorrUsed', 22, 23),
            ]),
        ]),
    ]),
    core.Message(0x32, 'SBAS', [
        core.Field('iTOW', 'U4'),
        core.Field('geo', 'U1'),
        core.Field('mode', 'U1'),
        core.Field('sys', 'I1'),
        core.BitField('service', 'X1', [
            core.Flag('ranging', 0, 1),
            core.Flag('corrections', 1, 2),
            core.Flag('integrity', 2, 3),
            core.Flag('testMode', 3, 4),
            core.Flag('bad', 4, 5),
        ]),
        core.Field('cnt', 'U1'),
        core.PadByte(repeat=2),
        core.RepeatedBlock('RB', [
            core.Field('svid', 'U1'),
            core.Field('flags', 'U1'),
            core.Field('udre', 'U1'),
            core.Field('svSys', 'U1'),
            core.Field('svService', 'U1'),
            core.PadByte(),
            core.Field('prc', 'I2'),
            core.PadByte(repeat=1),
            core.Field('ic', 'I2'),
        ]),
    ]),
    core.Message(0x42, 'SLAS', [
        core.Field('iTOW', 'U4'),
        core.Field('version', 'U1'),
        core.PadByte(repeat=2),
        core.Field('gmsLon', 'I4'),
        core.Field('gmsLat', 'I4'),
        core.Field('gmsCode', 'U1'),
        core.Field('qzssSvId', 'U1'),
        core.BitField('serviceFlags', 'X1', [
            core.Flag('gmsAvail', 0, 1),
            core.Flag('qzssSvAvail', 1, 2),
            core.Flag('testMode', 2, 3),
        ]),
        core.Field('cnt', 'U1'),
        core.RepeatedBlock('RB', [
            core.Field('gnssId', 'U1'),
            core.Field('svId', 'U1'),
            core.PadByte(repeat=3),
            core.Field('prc', 'I2'),
        ])
    ]),
    core.Message(0x03, 'STATUS', [
        core.Field('iTOW', 'U4'),
        core.Field('gpsFix', 'U1'),
        core.BitField('flags', 'X1', [
            core.Flag('gpsFixOK', 0, 1),
            core.Flag('diffSoln', 1, 2),
            core.Flag('wknSet', 2, 3),
            core.Flag('towSet', 3, 4),
        ]),
        core.BitField('fixStat', 'X1', [
            core.Flag('diffCorr', 0, 1),
            core.Flag('mapMatching', 6, 8),
        ]),
        core.BitField('flags2', 'X1', [
            core.Flag('psmState', 0, 2),
            core.Flag('spoofDetState', 3, 5),
        ]),
        core.Field('ttff', 'U4'),
        core.Field('msss', 'U4'),
    ]),
    core.Message(0x06, 'SOL', [
        core.Field('iTOW', 'U4'),
        core.Field('fTOW', 'I4'),
        core.Field('week', 'I2'),
        core.Field('gpsFix', 'U1'),
        core.BitField('flags', 'X1', [
            core.Flag('gpsFixOK', 0, 1),
            core.Flag('diffSoln', 1, 2),
            core.Flag('wknSet', 2, 3),
            core.Flag('towSet', 3, 4),
        ]),
        core.Field('ecefX', 'I4'),
        core.Field('ecefY', 'I4'),
        core.Field('ecefZ', 'I4'),
        core.Field('pAcc', 'U4'),
        core.Field('ecefVX', 'I4'),
        core.Field('ecefVY', 'I4'),
        core.Field('ecefVZ', 'I4'),
        core.Field('sAcc', 'U4'),
        core.Field('pDOP', 'U2'),
        core.PadByte(),
        core.Field('numSV', 'U1'),
        core.PadByte(repeat=3),
    ]),
    core.Message(0x30, 'SVINFO', [
        core.Field('iTOW', 'U4'),
        core.Field('numCh', 'U1'),
        core.BitField('globalFlags', 'X1', [
            core.Flag('chipGen', 0, 3),
        ]),
        core.PadByte(repeat=1),
        core.RepeatedBlock('RB', [
            core.Field('chn', 'U1'),
            core.Field('svid', 'U1'),
            core.BitField('flags', 'X1', [
                core.Flag('svUsed', 0, 1),
                core.Flag('diffCorr', 1, 2),
                core.Flag('orbitAvail', 2, 3),
                core.Flag('orbitEph', 3, 4),
                core.Flag('unhealthy', 4, 5),
                core.Flag('orbitAlm', 5, 6),
                core.Flag('orbitAop', 6, 7),
                core.Flag('smoothed', 7, 8),
            ]),
            core.BitField('quality', 'X1', [
                core.Flag('qualityInd', 0, 4),
            ]),
            core.Field('cno', 'U1'),
            core.Field('elev', 'I1'),
            core.Field('azim', 'I2'),
            core.Field('prRes', 'I4'),
        ]),
    ]),
    core.Message(0x21, 'TIMEUTC', [
        core.Field('iTOW', 'U4'),
        core.Field('tAcc', 'U4'),
        core.Field('nano', 'I4'),
        core.Field('year', 'U2'),
        core.Field('month', 'U1'),
        core.Field('day', 'U1'),
        core.Field('hour', 'U1'),
        core.Field('min', 'U1'),
        core.Field('sec', 'U1'),
        core.BitField('valid', 'X1', [
            core.Flag('validTOW', 0, 1),
            core.Flag('validWKN', 1, 2),
            core.Flag('validUTC', 2, 3),
            core.Flag('utcStandard', 4, 8),
        ]),
    ]),
    core.Message(0x11, 'VELECEF', [
        core.Field('iTOW', 'U4'),
        core.Field('ecefVX', 'I4'),
        core.Field('ecefVY', 'I4'),
        core.Field('ecefVZ', 'I4'),
        core.Field('sAcc', 'U4'),
    ]),
    core.Message(0x12, 'VELNED', [
        core.Field('iTOW', 'U4'),
        core.Field('velN', 'I4'),
        core.Field('velE', 'I4'),
        core.Field('velD', 'I4'),
        core.Field('speed', 'U4'),
        core.Field('gSpeed', 'U4'),
        core.Field('heading', 'I4'),
        core.Field('sAcc', 'U4'),
        core.Field('cAcc', 'U4'),
    ]),
    core.Message(0x62, 'PL', [
        core.Field('msgVersion', 'U1'),
        core.Field('tmirCoeff', 'U1'),
        core.Field('tmirExp', 'I1'),
        core.Field('plPosValid', 'U1'),
        core.Field('plPosFrame', 'U1'),
        core.Field('plVelValid', 'U1'),
        core.Field('plVelFrame', 'U1'),
        core.Field('plTimeValid', 'U1'),
        core.PadByte(repeat=3),
        core.Field('iTow', 'U4'),
        core.Field('plPos1', 'U4'),
        core.Field('plPos2', 'U4'),
        core.Field('plPos3', 'U4'),
        core.Field('plVel1', 'U4'),
        core.Field('plVel2', 'U4'),
        core.Field('plVel3', 'U4'),
        core.Field('plPosHorizOrient', 'U2'),
        core.Field('plVelHorizOrient', 'U2'),
        core.Field('plTime', 'U4'),
        core.PadByte(repeat=3),
    ])
])

RXM_CLS = core.Cls(0x02, 'RXM', [
    core.Message(0x13, 'SFRBX', [
        core.Field('gnssId', 'U1'),
        core.Field('svId', 'U1'),
        core.Field('sigId', 'U1'),
        core.Field('freqId', 'U1'),
        core.Field('numWords', 'U1'),
        core.Field('chn', 'U1'),
        core.Field('version', 'U1'),
        core.PadByte(),
        core.RepeatedBlock('RB', [
            core.Field('dwrd', 'U4'),
        ]),
    ]),
    core.Message(0x15, 'RAWX', [
        core.Field('rcvTOW', 'R8'),
        core.Field('week', 'U2'),
        core.Field('leapS', 'I1'),
        core.Field('numMeas', 'U1'),
        core.BitField('recStat', 'X1', [
            core.Flag('leapSec', 0, 1),
            core.Flag('clkReset', 1, 2),
        ]),
        core.Field('version', 'U1'),
        core.PadByte(repeat=1),
        core.RepeatedBlock('RB', [
            core.Field('prMes', 'R8'),
            core.Field('cpMes', 'R8'),
            core.Field('doMes', 'R4'),
            core.Field('gnssId', 'U1'),
            core.Field('svId', 'U1'),
            core.Field('sigId', 'U1'),
            core.Field('freqId', 'U1'),
            core.Field('locktime', 'U2'),
            core.Field('cno', 'U1'),
            core.BitField('prStdev', 'X1', [
                core.Flag('prStd', 0, 4),
            ]),
            core.BitField('cpStdev', 'X1', [
                core.Flag('cpStd', 0, 4),
            ]),
            core.BitField('doStdev', 'X1', [
                core.Flag('doStd', 0, 4),
            ]),
            core.BitField('trkStat', 'X1', [
                core.Flag('prValid', 0, 1),
                core.Flag('cpValid', 1, 2),
                core.Flag('halfCyc', 2, 3),
                core.Flag('subHalfCyc', 3, 4),
            ]),
            core.PadByte()
        ])
    ])
])


MON_CLS = core.Cls(0x0A, 'MON', [
    core.Message(0x09, 'HW', [
        core.Field('pinSel', 'U4'),
        core.Field('pinBank', 'U4'),
        core.Field('pinDir', 'U4'),
        core.Field('pinVal', 'U4'),
        core.Field('noisePerMS', 'U2'),
        core.Field('agcCnt', 'U2'),
        core.Field('aStatus', 'U1'),
        core.Field('aPower', 'U1'),
        core.Field('flags', 'U1'),
        core.PadByte(),
        core.Field('usedMask', 'U4'),
        core.RepeatedBlock('RB', [
            core.Field('VP', 'U1'),
        ]),
        core.Field('jamInd', 'U1'),
        core.PadByte(repeat=1),
        core.Field('pinIrq', 'U4'),
        core.Field('pullH', 'U4'),
        core.Field('pullL', 'U4')
    ])
])


ESF_CLS = core.Cls(0x10, 'ESF', [
    core.Message(0x02, 'MEAS', [
        core.Field('time_tag', 'U4'),
        core.BitField('flags', 'X2', [
            core.Flag('timeMarkSent', 0, 2),
            core.Flag('timeMarkEdge', 2, 3),
            core.Flag('calibTtagValid', 3, 4),
            core.Flag('numMeas', 11, 16)
        ]),
        core.Field('id', 'U2'),
        core.RepeatedBlock('RB', [
            core.BitField('data', 'X4', [
                core.Flag('dataField', 0, 24),
                core.Flag('dataType', 24, 30)
            ]),
        ]),
        core.Field('calib_tag', 'U4')
    ]),
    core.Message(0x03, 'RAW', [
        core.Field('msss', 'U4'),
        core.RepeatedBlock('RB', [
            core.BitField('data', 'X4', [
                core.Flag('dataField', 0, 24),
                core.Flag('dataType', 24, 30)
            ]),
            core.Field('sensor_time_tag', 'U4')
        ])
    ]),
    core.Message(0x15, 'INS', [
        core.Field('bitfield0', 'U4'),
        core.PadByte(repeat=3),
        core.Field('i_tow', 'U4'),
        core.Field('x_ang_rate', 'I4'),
        core.Field('y_ang_rate', 'I4'),
        core.Field('z_ang_rate', 'I4'),
        core.Field('x_accel', 'I4'),
        core.Field('y_accel', 'I4'),
        core.Field('z_accel', 'I4')
    ])
])

