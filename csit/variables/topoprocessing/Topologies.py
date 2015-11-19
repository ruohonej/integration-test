NETWORK_UNDERLAY_TOPOLOGY_1 = '''<topology
                                xmlns="urn:TBD:params:xml:ns:yang:network-topology"
                                xmlns:pcep="urn:opendaylight:params:xml:ns:yang:topology:pcep"
                                xmlns:ovsdb="urn:opendaylight:params:xml:ns:yang:ovsdb">
                            <topology-id>network-topo:1</topology-id>
                            <topology-types>
                                <pcep:topology-pcep></pcep:topology-pcep>
                            </topology-types>
                            <node>
                                <node-id>pcep:1</node-id>
                                <pcep:path-computation-client>
                                    <pcep:ip-address>192.168.1.1</pcep:ip-address>
                                </pcep:path-computation-client>
                                <termination-point>
                                    <tp-id>tp:1:1</tp-id>
                                    <ovsdb:ofport>1119</ovsdb:ofport>
                                </termination-point>
                                <termination-point>
                                    <tp-id>tp:1:2</tp-id>
                                    <ovsdb:ofport>1119</ovsdb:ofport>
                                </termination-point>
                                <termination-point>
                                    <tp-id>tp:1:3</tp-id>
                                    <ovsdb:ofport>2119</ovsdb:ofport>
                                </termination-point>
                            </node>
                            <node>
                                <node-id>pcep:2</node-id>
                                <pcep:path-computation-client>
                                    <pcep:ip-address>192.168.1.2</pcep:ip-address>
                                </pcep:path-computation-client>
                            </node>
                            <node>
                                <node-id>pcep:3</node-id>
                                <pcep:path-computation-client>
                                    <pcep:ip-address>192.168.2.1</pcep:ip-address>
                                </pcep:path-computation-client>
                                <termination-point>
                                    <tp-id>tp:3:1</tp-id>
                                    <ovsdb:ofport>1118</ovsdb:ofport>
                                </termination-point>
                                <termination-point>
                                    <tp-id>tp:3:2</tp-id>
                                    <ovsdb:ofport>2118</ovsdb:ofport>
                                </termination-point>
                            </node>
                            <node>
                                <node-id>pcep:4</node-id>
                                <pcep:path-computation-client>
                                    <pcep:ip-address>192.168.2.1</pcep:ip-address>
                                </pcep:path-computation-client>
                                <termination-point>
                                    <tp-id>tp:4:1</tp-id>
                                    <ovsdb:ofport>1117</ovsdb:ofport>
                                </termination-point>
                                <termination-point>
                                    <tp-id>tp:4:2</tp-id>
                                    <ovsdb:ofport>1117</ovsdb:ofport>
                                </termination-point>
                            </node>
                            <node>
                                <node-id>pcep:5</node-id>
                                <pcep:path-computation-client>
                                    <pcep:ip-address>192.168.2.3</pcep:ip-address>
                                </pcep:path-computation-client>
                                <termination-point>
                                    <tp-id>tp:5:1</tp-id>
                                    <ovsdb:ofport>1116</ovsdb:ofport>
                                </termination-point>
                            </node>
                        </topology>'''

NETWORK_UNDERLAY_TOPOLOGY_2 = '''<topology
                                xmlns="urn:TBD:params:xml:ns:yang:network-topology"
                                xmlns:pcep="urn:opendaylight:params:xml:ns:yang:topology:pcep"
                                xmlns:ovsdb="urn:opendaylight:params:xml:ns:yang:ovsdb">
                            <topology-id>network-topo:2</topology-id>
                            <topology-types>
                                <pcep:topology-pcep></pcep:topology-pcep>
                            </topology-types>
                            <node>
                                <node-id>pcep:6</node-id>
                                <pcep:path-computation-client>
                                    <pcep:ip-address>192.168.1.3</pcep:ip-address>
                                </pcep:path-computation-client>
                                <termination-point>
                                    <tp-id>tp:6:1</tp-id>
                                    <ovsdb:ofport>1116</ovsdb:ofport>
                                </termination-point>
                            </node>
                            <node>
                                <node-id>pcep:7</node-id>
                                <pcep:path-computation-client>
                                    <pcep:ip-address>192.168.1.4</pcep:ip-address>
                                </pcep:path-computation-client>
                                <termination-point>
                                    <tp-id>tp:7:1</tp-id>
                                    <ovsdb:ofport>1117</ovsdb:ofport>
                                </termination-point>
                            </node>
                            <node>
                                <node-id>pcep:8</node-id>
                                <pcep:path-computation-client>
                                    <pcep:ip-address>192.168.2.4</pcep:ip-address>
                                </pcep:path-computation-client>
                                <termination-point>
                                    <tp-id>tp:8:1</tp-id>
                                    <ovsdb:ofport>11120</ovsdb:ofport>
                                </termination-point>
                            </node>
                            <node>
                                <node-id>pcep:9</node-id>
                                <pcep:path-computation-client>
                                    <pcep:ip-address>192.168.2.5</pcep:ip-address>
                                </pcep:path-computation-client>
                                <termination-point>
                                    <tp-id>tp:9:1</tp-id>
                                    <ovsdb:ofport>1121</ovsdb:ofport>
                                </termination-point>
                            </node>
                            <node>
                                <node-id>pcep:10</node-id>
                                <pcep:path-computation-client>
                                    <pcep:ip-address>192.168.2.3</pcep:ip-address>
                                </pcep:path-computation-client>
                                <termination-point>
                                    <tp-id>tp:10:1</tp-id>
                                    <ovsdb:ofport>1122</ovsdb:ofport>
                                </termination-point>
                            </node>
                        </topology>'''

OPENFLOW_UNDERLAY_NODES = '''
<nodes
    xmlns="urn:opendaylight:inventory"
    xmlns:flov-inv="urn:opendaylight:flow:inventory">
    <node>
        <id>openflow:1</id>
        <node-connector>
            <id>openflow:1:1</id>
            <flov-inv:port-number>1</flov-inv:port-number>
        </node-connector>
        <node-connector>
            <id>openflow:1:2</id>
            <flov-inv:port-number>1</flov-inv:port-number>
        </node-connector>
        <flov-inv:manufacturer>Pantheon Technologies</flov-inv:manufacturer>
        <flov-inv:ip-address>192.168.1.1</flov-inv:ip-address>
    </node>
    <node>
        <id>openflow:2</id>
        <node-connector>
            <id>openflow:2:1</id>
            <flov-inv:port-number>1</flov-inv:port-number>
        </node-connector>
        <node-connector>
            <id>openflow:2:2</id>
            <flov-inv:port-number>2</flov-inv:port-number>
        </node-connector>
        <flov-inv:manufacturer>Pantheon Technologies</flov-inv:manufacturer>
        <flov-inv:ip-address>192.168.1.2</flov-inv:ip-address>
    </node>
    <node>
        <id>openflow:3</id>
        <node-connector>
            <id>openflow:3:1</id>
            <flov-inv:port-number>2</flov-inv:port-number>
        </node-connector>
        <node-connector>
            <id>openflow:3:2</id>
            <flov-inv:port-number>2</flov-inv:port-number>
        </node-connector>
        <node-connector>
            <id>openflow:3:3</id>
            <flov-inv:port-number>1</flov-inv:port-number>
        </node-connector>
        <flov-inv:manufacturer>Pantheon Technologies</flov-inv:manufacturer>
        <flov-inv:ip-address>192.168.1.3</flov-inv:ip-address>
    </node>
    <node>
        <id>openflow:4</id>
        <node-connector>
            <id>openflow:4:1</id>
            <flov-inv:port-number>1</flov-inv:port-number>
        </node-connector>
        <node-connector>
            <id>openflow:4:2</id>
            <flov-inv:port-number>1</flov-inv:port-number>
        </node-connector>
        <node-connector>
            <id>openflow:4:3</id>
            <flov-inv:port-number>1</flov-inv:port-number>
        </node-connector>
        <flov-inv:manufacturer>Cisco</flov-inv:manufacturer>
        <flov-inv:ip-address>192.168.2.1</flov-inv:ip-address>
    </node>
    <node>
        <id>openflow:5</id>
        <node-connector>
            <id>openflow:5:1</id>
            <flov-inv:port-number>3</flov-inv:port-number>
        </node-connector>
        <flov-inv:manufacturer>Cisco</flov-inv:manufacturer>
        <flov-inv:ip-address>192.168.2.2</flov-inv:ip-address>
    </node>
    <node>
        <id>openflow:6</id>
        <flov-inv:manufacturer>Pantheon Technologies</flov-inv:manufacturer>
        <flov-inv:ip-address>192.168.1.1</flov-inv:ip-address>
    </node>
    <node>
        <id>openflow:7</id>
        <flov-inv:manufacturer>Pantheon Technologies</flov-inv:manufacturer>
        <flov-inv:ip-address>192.168.2.3</flov-inv:ip-address>
    </node>
    <node>
        <id>openflow:8</id>
        <flov-inv:manufacturer>Cisco</flov-inv:manufacturer>
        <flov-inv:ip-address>192.168.1.4</flov-inv:ip-address>
    </node>
    <node>
        <id>openflow:9</id>
        <flov-inv:manufacturer>Cisco</flov-inv:manufacturer>
        <flov-inv:ip-address>192.168.2.3</flov-inv:ip-address>
    </node>
    <node>
        <id>openflow:10</id>
        <flov-inv:manufacturer>Cisco</flov-inv:manufacturer>
        <flov-inv:ip-address>192.168.2.1</flov-inv:ip-address>
    </node>
</nodes>
'''

OPENFLOW_UNDERLAY_TOPOLOGY_1 = '''
<topology
        xmlns="urn:TBD:params:xml:ns:yang:network-topology"
        xmlns:inventory="urn:opendaylight:inventory"
        xmlns:inventory-topo="urn:opendaylight:model:topology:inventory">
    <topology-id>openflow-topo:1</topology-id>
    <node>
        <node-id>of-node:1</node-id>
        <inventory-topo:inventory-node-ref>/inventory:nodes/inventory:node[inventory:id="openflow:1"]</inventory-topo:inventory-node-ref>
        <termination-point>
            <tp-id>tp:1:1</tp-id>
            <inventory-topo:inventory-node-connector-ref>
                /inventory:nodes/inventory:node[inventory:id="openflow:1"]/inventory:node-connector[inventory:id="openflow:1:1"]
            </inventory-topo:inventory-node-connector-ref>
        </termination-point>
        <termination-point>
            <tp-id>tp:1:2</tp-id>
            <inventory-topo:inventory-node-connector-ref>
                /inventory:nodes/inventory:node[inventory:id="openflow:1"]/inventory:node-connector[inventory:id="openflow:1:2"]
            </inventory-topo:inventory-node-connector-ref>
        </termination-point>
    </node>
    <node>
        <node-id>of-node:2</node-id>
        <inventory-topo:inventory-node-ref>/inventory:nodes/inventory:node[inventory:id="openflow:2"]</inventory-topo:inventory-node-ref>
        <termination-point>
            <tp-id>tp:2:1</tp-id>
            <inventory-topo:inventory-node-connector-ref>
                /inventory:nodes/inventory:node[inventory:id="openflow:2"]/inventory:node-connector[inventory:id="openflow:2:1"]
            </inventory-topo:inventory-node-connector-ref>
        </termination-point>
        <termination-point>
            <tp-id>tp:2:2</tp-id>
            <inventory-topo:inventory-node-connector-ref>
                /inventory:nodes/inventory:node[inventory:id="openflow:2"]/inventory:node-connector[inventory:id="openflow:2:2"]
            </inventory-topo:inventory-node-connector-ref>
        </termination-point>
    </node>
    <node>
        <node-id>of-node:3</node-id>
        <inventory-topo:inventory-node-ref>/inventory:nodes/inventory:node[inventory:id="openflow:3"]</inventory-topo:inventory-node-ref>
        <termination-point>
            <tp-id>tp:3:1</tp-id>
            <inventory-topo:inventory-node-connector-ref>
                /inventory:nodes/inventory:node[inventory:id="openflow:3"]/inventory:node-connector[inventory:id="openflow:3:1"]
            </inventory-topo:inventory-node-connector-ref>
        </termination-point>
        <termination-point>
            <tp-id>tp:3:2</tp-id>
            <inventory-topo:inventory-node-connector-ref>
                /inventory:nodes/inventory:node[inventory:id="openflow:3"]/inventory:node-connector[inventory:id="openflow:3:2"]
            </inventory-topo:inventory-node-connector-ref>
        </termination-point>
        <termination-point>
            <tp-id>tp:3:3</tp-id>
            <inventory-topo:inventory-node-connector-ref>
                /inventory:nodes/inventory:node[inventory:id="openflow:3"]/inventory:node-connector[inventory:id="openflow:3:3"]
            </inventory-topo:inventory-node-connector-ref>
        </termination-point>
    </node>
    <node>
        <node-id>of-node:4</node-id>
        <inventory-topo:inventory-node-ref>/inventory:nodes/inventory:node[inventory:id="openflow:4"]</inventory-topo:inventory-node-ref>
        <termination-point>
            <tp-id>tp:4:1</tp-id>
            <inventory-topo:inventory-node-connector-ref>
                /inventory:nodes/inventory:node[inventory:id="openflow:4"]/inventory:node-connector[inventory:id="openflow:4:1"]
            </inventory-topo:inventory-node-connector-ref>
        </termination-point>
        <termination-point>
            <tp-id>tp:4:2</tp-id>
            <inventory-topo:inventory-node-connector-ref>
                /inventory:nodes/inventory:node[inventory:id="openflow:4"]/inventory:node-connector[inventory:id="openflow:4:2"]
            </inventory-topo:inventory-node-connector-ref>
        </termination-point>
        <termination-point>
            <tp-id>tp:4:3</tp-id>
            <inventory-topo:inventory-node-connector-ref>
                /inventory:nodes/inventory:node[inventory:id="openflow:4"]/inventory:node-connector[inventory:id="openflow:4:3"]
            </inventory-topo:inventory-node-connector-ref>
        </termination-point>
    </node>
    <node>
        <node-id>of-node:5</node-id>
        <inventory-topo:inventory-node-ref>/inventory:nodes/inventory:node[inventory:id="openflow:5"]</inventory-topo:inventory-node-ref>
        <termination-point>
            <tp-id>tp:5:1</tp-id>
            <inventory-topo:inventory-node-connector-ref>
                /inventory:nodes/inventory:node[inventory:id="openflow:5"]/inventory:node-connector[inventory:id="openflow:5:1"]
            </inventory-topo:inventory-node-connector-ref>
        </termination-point>
    </node>
</topology>
'''

OPENFLOW_UNDERLAY_TOPOLOGY_2 = '''
<topology
        xmlns="urn:TBD:params:xml:ns:yang:network-topology"
        xmlns:inventory="urn:opendaylight:inventory"
        xmlns:inventory-topo="urn:opendaylight:model:topology:inventory">
    <topology-id>openflow-topo:2</topology-id>
    <node>
        <node-id>of-node:6</node-id>
        <inventory-topo:inventory-node-ref>/inventory:nodes/inventory:node[inventory:id="openflow:6"]</inventory-topo:inventory-node-ref>
    </node>
    <node>
        <node-id>of-node:7</node-id>
        <inventory-topo:inventory-node-ref>/inventory:nodes/inventory:node[inventory:id="openflow:7"]</inventory-topo:inventory-node-ref>
    </node>
    <node>
        <node-id>of-node:8</node-id>
        <inventory-topo:inventory-node-ref>/inventory:nodes/inventory:node[inventory:id="openflow:8"]</inventory-topo:inventory-node-ref>
    </node>
    <node>
        <node-id>of-node:9</node-id>
        <inventory-topo:inventory-node-ref>/inventory:nodes/inventory:node[inventory:id="openflow:9"]</inventory-topo:inventory-node-ref>
    </node>
    <node>
        <node-id>of-node:10</node-id>
        <inventory-topo:inventory-node-ref>/inventory:nodes/inventory:node[inventory:id="openflow:10"]</inventory-topo:inventory-node-ref>
    </node>
</topology>
'''
